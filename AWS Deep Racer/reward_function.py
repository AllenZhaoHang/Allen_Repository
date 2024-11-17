import math

def reward_function(params):
    '''
    Reward function to encourage the agent to stay within track boundaries and avoid collisions with objects.
    '''
    # Read parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    objects_location = params['objects_location']
    agent_x = params['x']
    agent_y = params['y']
    _, next_object_index = params['closest_objects']
    objects_left_of_center = params['objects_left_of_center']
    is_left_of_center = params['is_left_of_center']
    
    # Initialize reward
    reward = 1e-3
    
    # Reward for staying on track and close to center
    if all_wheels_on_track:
        # Assign more points based on distance from center, giving high reward when close to center
        center_factor = 1.0 - (distance_from_center / (0.5 * track_width))
        reward_lane = max(0.1, center_factor)
    else:
        reward_lane = 1e-3
    
    # Reward for avoiding collisions
    reward_avoid = 1.0
    next_object_loc = objects_location[next_object_index]
    distance_to_object = math.sqrt((agent_x - next_object_loc[0])**2 + (agent_y - next_object_loc[1])**2)
    
    # Penalize more if the agent and object are in the same lane and distance is close
    is_same_lane = objects_left_of_center[next_object_index] == is_left_of_center
    if is_same_lane:
        if distance_to_object < 0.3:
            reward_avoid = 1e-3  # Likely crash
        elif distance_to_object < 0.5:
            reward_avoid = 0.2
        elif distance_to_object < 0.8:
            reward_avoid = 0.5
    
    # Total reward is weighted sum of lane adherence and collision avoidance
    reward += 2.0 * reward_lane + 5.0 * reward_avoid
    
    return float(reward)
