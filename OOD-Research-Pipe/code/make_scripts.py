import argparse
import itertools

parser = argparse.ArgumentParser(description='config')
parser.add_argument('--run', default='train', type=str)
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


def make_controls(script_name, control_name):
    #control_names = []
    #for i in range(len(control_name)):
    #    control_names.extend(list('_'.join(x) for x in itertools.product(*control_name[i])))
    #controls = [control_names]
    controls = script_name + [control_name[0]] + [control_name[1]]
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
        data_name = ['cifar10']#, 'cifar100', 'mnist']
        attack_name = ['VANILA', 'GN', 'FGSM', 'BIM', 'RFGSM', 'PGD', 'EOTPGD', \
            'FFGSM', 'TPGD', 'MIFGSM', 'UPGD', 'APGD', 'APGDT', 'DIFGSM', 'TIFGSM', 'Jitter',\
            'NIFGSM', 'PGDRS', 'SINIFGSM', 'VMIFGSM', 'VNIFGSM', 'CW', 'PGDL2', 'PGDRSL2',\
            'DeepFool', 'SparseFool', 'OnePixel', 'Pixle', 'FAB', 'AutoAttack', 'Square',\
            'SPSA', 'JSMA', 'EADL1', 'EADEN', 'PIFGSM', 'PIFGSMPP']
        attack_name = ['JSMA', 'SparseFool', 'OnePixel', 'Square', 'DeepFool', 'Pixle']
        control_name = [attack_name, data_name]
        controls = make_controls(script_name, control_name)
        print(controls)
    else:
        raise ValueError('Not valid mode')

    s = '#!/bin/bash\n'
    s += 'python dir_prep.py\n'
    s += 'wait\n'
    j = 1
    k = 1
    for i in range(len(controls)):
        controls[i] = list(controls[i])
        s = s + 'CUDA_VISIBLE_DEVICES=\"{}\" python {} --attack_name {} --dataset {}' \
                '&\n'.format(gpu_ids[i % len(gpu_ids)], *controls[i])
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
