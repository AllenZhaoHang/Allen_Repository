import argparse
import itertools

parser = argparse.ArgumentParser(description='config')
parser.add_argument('--run', default='detectors_eval', type=str)
parser.add_argument('--init_gpu', default=0, type=int)
parser.add_argument('--num_gpus', default=4, type=int)
parser.add_argument('--init_seed', default=0, type=int)
parser.add_argument('--round', default=4, type=int)
parser.add_argument('--experiment_step', default=1, type=int)
parser.add_argument('--num_experiment', default=1, type=int)
parser.add_argument('--resume_mode', default=0, type=int)
parser.add_argument('--mode', default=None, type=str)
parser.add_argument('--split_round', default=65535, type=int)
args = vars(parser.parse_args())


# print(args)


def make_controls(script_name, model_list, dataset_list, attack_list, detector_list):
    #control_names = []
    #for i in range(len(control_name)):
    #    control_names.extend(list('_'.join(x) for x in itertools.product(*control_name[i])))
    #controls = [control_names]
    controls = script_name + [model_list] + [attack_list] + [dataset_list] + [detector_list]
    controls = list(itertools.product(*controls))
    return controls


def main():
    run = args['run']
    mode = args['mode']
    init_gpu = args['init_gpu']
    num_gpus = args['num_gpus']
    round = args['round']
    split_round = args['split_round']
    gpu_ids = [','.join(str(i) for i in list(range(x, x + 1))) for x in
               list(range(init_gpu, init_gpu + num_gpus))]

    filename = '{}_{}'.format(run, mode)
    if mode == 'base':
        script_name = [['{}.py'.format(run)]]
        model_list = ['WideResNet']
        dataset_list = ['cifar10'] #', 'cifar100', 'mnist']
        attack_list = ['PGD','FGSM']#, 'CW','BIM','PGDL2', 'Jitter', 'VMIFGSM', 'NIFGSM']
        '''attack_list = ['VANILA', 'GN', 'FGSM', 'BIM', 'RFGSM', 'PGD', 'EOTPGD', \
                                    'FFGSM', 'TPGD', 'MIFGSM', 'UPGD', 'APGD', 'APGDT', 'DIFGSM', 'TIFGSM', 'Jitter',\
                                    'NIFGSM', 'PGDRS', 'SINIFGSM', 'VMIFGSM', 'VNIFGSM', 'CW', 'PGDL2', 'PGDRSL2',\
                                    'DeepFool', 'SparseFool', 'OnePixel', 'Pixle', 'FAB', 'AutoAttack', 'Square',\
                                    'SPSA', 'JSMA', 'EADL1', 'EADEN', 'PIFGSM', 'PIFGSMPP']'''
        detector_list = ["ReAct", "OpenMax", "TemperatureScaling", "KNN", 'ODIN', 'EnergyBased', 'Entropy', 'KLMatching', 'Mahalanobis', 'Mahalanobis+ODIN',
                 'MaxLogit','ViM', 'RMD', 'DICE', 'SHE', "MSP", "MCD", "ASH"]
        # detector_list = ["OpenMax", ] 
        control_name = [model_list, dataset_list, attack_list, detector_list]
        controls = make_controls(script_name, model_list, dataset_list, attack_list, detector_list)
        # print(controls)
    else:
        raise ValueError('Not valid mode')

    print(controls)

    s = '#!/bin/bash\n'
    s += 'python dir_prep.py\n'
    s += 'wait\n'
    j = 1
    k = 1
    for i in range(len(controls)):
        controls[i] = list(controls[i])
        s = s + 'CUDA_VISIBLE_DEVICES=\"{}\" python {} --model {} --attack_data {}_{} --detector {}' \
                ' &\n'.format(gpu_ids[i % len(gpu_ids)], *controls[i])
        if i % round == round - 1:
            s = s[:-2] + '\nwait\n'
            if j % split_round == 0:
                print(s)
                run_file = open('{}_{}.sh'.format(filename, k), 'w')
                run_file.write(s)
                run_file.close()
                s = '#!/bin/bash\n'
                k = k + 1
            j = j + 1
    if s != '#!/bin/bash\n':
        if s[-5:-1] != 'wait':
            s = s + 'wait\n'
        print(s)
        run_file = open('{}_{}.sh'.format(filename, k), 'w')
        run_file.write(s)
        run_file.close()
    return


if __name__ == '__main__':
    main()
