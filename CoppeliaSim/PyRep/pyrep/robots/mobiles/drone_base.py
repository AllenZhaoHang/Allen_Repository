from pyrep.robots.mobiles.mobile_base import MobileBase
from pyrep.robots.configuration_paths.holonomic_configuration_path import (
    HolonomicConfigurationPath)
from pyrep.backend import utils
from pyrep.const import PYREP_SCRIPT_TYPE
from pyrep.const import ConfigurationPathAlgorithms as Algos
from pyrep.errors import ConfigurationPathError
from typing import List
from pyrep.objects.joint import Joint
from math import pi, sqrt
from pyrep.backend import vrep, utils
from pyrep.robots.robot_component import RobotComponent
from pyrep.objects.dummy import Dummy
from pyrep.objects.shape import Shape
import numpy as np




class DroneBase(RobotComponent):
    """Base class for representing drone movement."""
    def __init__(self,
                 count: int, 
                 num_propellers: int, 
                 distance_from_target: float, 
                 name: str):
        """Count is used for when we have multiple copies of mobile bases.

        :param count: used for multiple copies of robots
        :param num_propellers: number of actuated propellers
        :param name: string with robot name (same as base in vrep model).
        """
        joint_names = ['%s_propeller_joint%s' % (name, str(i + 1)) for i in
                range(num_propellers)]
        super().__init__(count, name, joint_names)

        self.dist1 = distance_from_target
        self.num_propellers = num_propellers
        self.static_propeller_velocity = 5.335
        self.pParam=2
        self.iParam=0
        self.dParam=0
        self.vParam=-2
        self.cumul=0
        self.lastE=0
        self.pAlphaE=0
        self.pBetaE=0
        self.psp2=0
        self.psp1=0
        self.prevEuler=0

        suffix = '' if count == 0 else '#%d' % (count - 1)

        propeller_names = ['%s_propeller_respondable%s%s' % (name, str(i + 1), suffix) for i in
                       range(self.num_propellers)]

        self.propellers = self.get_propeller_handles(propeller_names)  # use handles instead of shapes here

        # Motion planning handles
        self.intermediate_target_base = Dummy(
            '%s_intermediate_target_base%s' % (name, suffix))
        self.target_base = Shape('%s_target_base%s' % (name, suffix))

        self._object_base = vrep.simGetObjectHandle(  
            '%s_base%s' % (name, suffix))   # object instead of collection of objects for quadracopter

        # Robot parameters and handle
        self.z_pos = self.get_position()[2]
        self.target_z = self.target_base.get_position()[-1]

    def get_propeller_handles(self, propeller_names: List[str]):
        """ Gets handles of propellers according to their names. 

        :param: A List containing the names of propellers (str).
        :return: A List containing the handles of propellers.
        """
        propellers=[]  # get handles of propellers
        for i in range(self.num_propellers):
            propellers.append(vrep.simGetScriptHandle(propeller_names[i]))
        return propellers

    def set_cartesian_position(self, position: List[float]):
        self.set_position(position)

    def get_cartesian_position(self):
        return self.get_position()

    def set_propeller_velocities(self, velocities: List[float]):
        """ Sets the particle velocities of propellers.

        :param velocities: A List containing the particle velocities for propellers.
        """
        for j in range(self.num_propellers):
            vrep.simSetScriptSimulationParameter(self.propellers[j],'particleVelocity',velocities[j])

    def get_2d_pose(self) -> List[float]: 
        """Gets the 2D (top-down) pose of the robot [x, y, yaw].

        :return: A List containing the x, y, yaw (in radians).
        """
        return (self.get_position()[:2] +
                self.get_orientation()[-1:])

    def set_2d_pose(self, pose: List[float]) -> None:
        """Sets the 2D (top-down) pose of the robot [x, y, yaw]

        :param pose: A List containing the x, y, yaw (in radians).
        """
        x, y, yaw = pose
        self.set_position([x, y, self.z_pos])
        self.set_orientation([0, 0, yaw])

    def get_3d_pose(self) -> List[float]:  # 
        """Gets the 3D pose of the robot [x, y, z, yaw].

        :return: A List containing the x, y, z, yaw (in radians).
        """
        return (self.get_position()[:3] +
                self.get_orientation()[-1:])

    def set_3d_pose(self, pose: List[float]) -> None:
        """Sets the 3D pose of the robot [x, y, z, yaw]

        :param pose: A List containing the x, y, z, yaw (in radians).
        """
        x, y, z, yaw = pose
        self.set_position([x, y, z])
        self.set_orientation([0, 0, yaw])

    def assess_collision(self):
        """Silent detection of the robot base with all other entities present in the scene.

        :return: True if collision is detected
        """
        return vrep.simCheckCollision(self._object_base,
                                      vrep.sim_handle_all) == 1

    def get_linear_path(self, position: List[float],
                            angle=0) -> HolonomicConfigurationPath:
        """Initialize linear path and check for collision along it.

        Must specify either rotation in euler or quaternions, but not both!

        :param position: The x, y position of the target.
        :param angle: The z orientation of the target (in radians).
        :raises: ConfigurationPathError if no path could be created.

        :return: A linear path in the 2d space.
        """
        position_base = self.get_position()
        angle_base = self.get_orientation()[-1]

        self.target_base.set_position(
            [position[0], position[1], self.target_z])
        self.target_base.set_orientation([0, 0, angle])

        handle_base = self.get_handle()
        handle_target_base = self.target_base.get_handle()
        _, ret_floats, _, _ = utils.script_call(
            'getBoxAdjustedMatrixAndFacingAngle@PyRep', PYREP_SCRIPT_TYPE,
            ints=[handle_base, handle_target_base])

        m = ret_floats[:-1]
        angle = ret_floats[-1]
        self.intermediate_target_base.set_position(
            [m[3] - m[0] * self.dist1, m[7] - m[4] * self.dist1,
            self.target_z])
        self.intermediate_target_base.set_orientation([0, 0, angle])
        self.target_base.set_orientation([0, 0, angle])

        path = [[position_base[0], position_base[1], angle_base],
                [position[0], position[1], angle]]

        if self._check_collision_linear_path(path):
            raise ConfigurationPathError(
                'Could not create path. '
                'An object was detected on the linear path.')

        return HolonomicConfigurationPath(self, path)

    def get_nonlinear_path(self, position: List[float],
                           angle=0,
                           boundaries=2,
                           path_pts=600,
                           ignore_collisions=False,
                           algorithm=Algos.RRTConnect
                            ) -> HolonomicConfigurationPath:
        """Gets a non-linear (planned) configuration path given a target pose.

        :param position: The x, y, z position of the target.
        :param angle: The z orientation of the target (in radians).
        :param boundaries: A float defining the path search in x and y direction
            [[-boundaries,boundaries],[-boundaries,boundaries]].
        :param path_pts: The number of sampled points returned from the
            computed path
        :param ignore_collisions: If collision checking should be disabled.
        :param algorithm: Algorithm used to compute path
        :raises: ConfigurationPathError if no path could be created.

        :return: A non-linear path (x,y,angle) in the xy configuration space.
        """

        path = self._get_nonlinear_path_points(
            position, angle, boundaries, path_pts, ignore_collisions, algorithm)

        return HolonomicConfigurationPath(self, path)

    def _get_nonlinear_path_points(self, position: List[float],
                           angle=0,
                           boundaries=2,
                           path_pts=600,
                           ignore_collisions=False,
                           algorithm=Algos.RRTConnect) -> List[List[float]]:
        """Gets a non-linear (planned) configuration path given a target pose.

        :param position: The x, y, z position of the target.
        :param angle: The z orientation of the target (in radians).
        :param boundaries: A float defining the path search in x and y direction
        [[-boundaries,boundaries],[-boundaries,boundaries]].
        :param path_pts: number of sampled points returned from the computed path
        :param ignore_collisions: If collision checking should be disabled.
        :param algorithm: Algorithm used to compute path
        :raises: ConfigurationPathError if no path could be created.

        :return: A non-linear path (x,y,angle) in the xy configuration space.
        """

        # Base dummy required to be parent of the robot tree
        # self.base_ref.set_parent(None)
        # self.set_parent(self.base_ref)

        # Missing the dist1 for intermediate target

        self.target_base.set_position([position[0], position[1], self.target_z])
        self.target_base.set_orientation([0, 0, angle])

        handle_base = self.get_handle()
        handle_target_base = self.target_base.get_handle()

        # Despite verbosity being set to 0, OMPL spits out a lot of text
        with utils.suppress_std_out_and_err():
            _, ret_floats, _, _ = utils.script_call(
                'getNonlinearPathMobile@PyRep', PYREP_SCRIPT_TYPE,
                ints=[handle_base, handle_target_base,
                      self._object_base,
                      int(ignore_collisions), path_pts], floats=[boundaries],
                      strings=[algorithm.value])

        # self.set_parent(None)
        # self.base_ref.set_parent(self)

        if len(ret_floats) == 0:
            raise ConfigurationPathError('Could not create path.')

        path = []
        for i in range(0, len(ret_floats) // 3):
            inst = ret_floats[3 * i:3 * i + 3]
            if i > 0:
                dist_change = sqrt((inst[0] - prev_inst[0]) ** 2 + (
                inst[1] - prev_inst[1]) ** 2)
            else:
                dist_change = 0
            inst.append(dist_change)

            path.append(inst)

            prev_inst = inst

        return path

    def _check_collision_linear_path(self,path):
        """Check for collision on a linear path from start to goal

        :param path: A list containing start and goal as [x,y,yaw]
        :return: A bool, True if collision was detected
        """
        start = path[0]
        end = path[1]

        m = (end[1] - start[1])/(end[0] - start[0])
        b = start[1] - m * start[0]
        x_range = [start[0],end[0]]
        x_span = start[0] - end[0]

        incr = round(abs(x_span)/50, 3)
        if x_range[1] < x_range[0]:
            incr = - incr

        x = x_range[0]
        for k in range(50):
            x += incr
            y = m * x + b
            self.set_2d_pose([x,y,start[-1] if k < 46 else end[-1]])
            status_collision = self.assess_collision()
            if status_collision == True:
                break

        return status_collision

    def get_base_actuation(self):
        """PIDV controller.

        :return: A list with actuations including thrust and three other values,
            and a bool representing target is reached.
        """

        relative_targetPos = self.target_base.get_position(relative_to=self)
        relative_targetOri= self.get_orientation(relative_to=self)
        if (sqrt((relative_targetPos[0]) ** 2 + (
        relative_targetPos[1]) ** 2) - self.dist1) < 0.1 and relative_targetOri[-1] < 0.1 * np.pi / 180:
            return [0, 0, 0, 0], True

        # Vertical control:
        targetPos=self.intermediate_target_base.get_position()
        pos=self.get_position()
        l, _=vrep.simGetVelocity(self.get_handle())
        e=(targetPos[2]-pos[2])
        self.cumul=self.cumul+e
        pv=self.pParam*e
        thrust=self.static_propeller_velocity+pv+self.iParam*self.cumul+self.dParam*(e-self.lastE)+l[2]*self.vParam

        self.lastE=e
        
        # Horizontal control: 
        sp=self.intermediate_target_base.get_position(relative_to=self)
        m=vrep.simGetObjectMatrix(self.get_handle(), -1)
        vx=[1,0,0,1]
        vx=np.matmul(np.array(m+[0,0,0,1]).reshape(4,4), vx)[:3]
        vy=[0,1,0,1]
        vy=np.matmul(np.array(m+[0,0,0,1]).reshape(4,4), vy)[:3]
        alphaE=(vy[2]-m[11])
        alphaCorr=0.25*alphaE+2.1*(alphaE-self.pAlphaE)
        betaE=(vx[2]-m[11])
        betaCorr=-0.25*betaE-2.1*(betaE-self.pBetaE)
        self.pAlphaE=alphaE
        self.pBetaE=betaE
        alphaCorr=alphaCorr+sp[1]*0.005+1*(sp[1]-self.psp2)
        betaCorr=betaCorr-sp[0]*0.005-1*(sp[0]-self.psp1)
        self.psp2=sp[1]
        self.psp1=sp[0]
        
        # Rotational control:
        euler=self.get_orientation(relative_to=self.intermediate_target_base)
        rotCorr=euler[2]*0.1+2*(euler[2]-self.prevEuler)
        self.prevEuler=euler[2]

        return [thrust, alphaCorr, betaCorr, rotCorr], False


    def set_base_angular_velocites(self, params: List[float]): 
        """Calls required functions to achieve desired omnidirectional effect.
        The name should be changed to be set_base_particle_velocites!

        :param params: A List with thrust and three factors for moving. 
        """
        assert self.num_propellers == 4
        particlesTargetVelocities = [0,0,0,0]
        thrust = params[0]
        alphaCorr = params[1]
        betaCorr = params[2]
        rotCorr = params[3]
        particlesTargetVelocities[0] = thrust*(1-alphaCorr+betaCorr+rotCorr)
        particlesTargetVelocities[1]=thrust*(1-alphaCorr-betaCorr-rotCorr)
        particlesTargetVelocities[2]=thrust*(1+alphaCorr-betaCorr+rotCorr)
        particlesTargetVelocities[3]=thrust*(1+alphaCorr+betaCorr-rotCorr)
        self.set_propeller_velocities(particlesTargetVelocities)
