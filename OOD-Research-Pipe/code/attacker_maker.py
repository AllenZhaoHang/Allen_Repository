import torchattacks

def make_attacker(attacker_name, model):
    if attacker_name == 'VANILA':
        attacker = torchattacks.VANILA(model)
    elif attacker_name == 'GN':
        attacker = torchattacks.GN(model)
    elif attacker_name == 'FGSM':
        attacker = torchattacks.FGSM(model, eps=8/255)
    elif attacker_name == 'BIM':
        attacker = torchattacks.BIM(model, eps=8 / 255, alpha=2 / 255, steps=10)
    elif attacker_name == 'RFGSM':
        attacker = torchattacks.RFGSM(model, eps=8/255, alpha=2/255, steps=10)
    elif attacker_name == 'PGD':
        attacker = torchattacks.PGD(model, eps=8/255, alpha=2/225, steps=10, random_start=True)
    elif attacker_name == 'EOTPGD':
        attacker = torchattacks.EOTPGD(model, eps=8/255, alpha=2/255, steps=10, eot_iter=2)
    elif attacker_name == 'FFGSM':
        attacker = torchattacks.FFGSM(model, eps=8/255, alpha=10/255)
    elif attacker_name == 'TPGD':
        attacker = torchattacks.TPGD(model, eps=8/255, alpha=2/255, steps=10)
    elif attacker_name == 'MIFGSM':
        attacker = torchattacks.MIFGSM(model, eps=8/255, steps=10, decay=1.0)
    elif attacker_name == 'UPGD':
        attacker = torchattacks.UPGD(model, eps=8/255, alpha=2/255, steps=10, random_start=False)
    elif attacker_name == 'APGD':
        attacker = torchattacks.APGD(model, norm='Linf', eps=8/255, steps=10, n_restarts=1, seed=0, loss='ce', eot_iter=1, rho=.75, verbose=False)
    elif attacker_name == 'APGDT':
        attacker = torchattacks.APGDT(model, norm='Linf', eps=8/255, steps=10, n_restarts=1, seed=0, eot_iter=1, rho=.75, verbose=False, n_classes=10)
    elif attacker_name == 'DIFGSM':
        attacker = torchattacks.DIFGSM(model, eps=8/255, alpha=2/255, steps=10, decay=0.0, resize_rate=0.9, diversity_prob=0.5, random_start=False)
    elif attacker_name == 'TIFGSM':
        attacker = torchattacks.TIFGSM(model, eps=8/255, alpha=2/255, steps=10, decay=1.0, resize_rate=0.9, diversity_prob=0.7, random_start=False)
    elif attacker_name == 'Jitter':
        attacker = torchattacks.Jitter(model, eps=8/255, alpha=2/255, steps=10, scale=10, std=0.1, random_start=True)
    elif attacker_name == 'NIFGSM':
        attacker = torchattacks.NIFGSM(model, eps=8/255, alpha=2/255, steps=10, decay=1.0)
    elif attacker_name == 'PGDRS':
        attacker = torchattacks.PGDRS(model, eps=8/255, alpha=2/255, steps=10, noise_type="guassian", noise_sd=0.5, noise_batch_size=5, batch_max=2048)
    elif attacker_name == 'SINIFGSM':
        attacker = torchattacks.SINIFGSM(model, eps=8/255, alpha=2/255, steps=10, decay=1.0, m=5)
    elif attacker_name == 'VMIFGSM':
        attacker = torchattacks.VMIFGSM(model, eps=8/255, alpha=2/255, steps=10, decay=1.0, N=5, beta=3/2)
    elif attacker_name == 'VNIFGSM':
        attacker = torchattacks.VNIFGSM(model, eps=8/255, alpha=2/255, steps=10, decay=1.0, N=5, beta=3/2)
    elif attacker_name == 'CW':
        attacker = torchattacks.CW(model, c=1, kappa=0, steps=100, lr=0.01)
    elif attacker_name == 'PGDL2':
        attacker = torchattacks.PGDL2(model, eps=128/255, alpha=15/255, steps=10, random_start=False)
    elif attacker_name == 'PGDRSL2':
        attacker = torchattacks.PGDRSL2(model, eps=1.0, alpha=0.2, steps=10, noise_type="guassian", noise_sd=0.5, noise_batch_size=5, batch_max=2048)
    elif attacker_name == 'DeepFool':
        attacker = torchattacks.DeepFool(model, steps=50, overshoot=0.02)
    elif attacker_name == 'SparseFool':
        attacker = torchattacks.SparseFool(model, steps=10, lam=3, overshoot=0.02)
    elif attacker_name == 'OnePixel':
        attacker = torchattacks.OnePixel(model, pixels=1, steps=10, popsize=10, inf_batch=128)
    elif attacker_name == 'Pixle':
        attacker = torchattacks.Pixle(model, x_dimensions=(0.1, 0.2), restarts=10, max_iterations=50)
    elif attacker_name == 'FAB':
        attacker = torchattacks.FAB(model, norm='Linf', steps=10, eps=8/255, n_restarts=1, alpha_max=0.1, eta=1.05, beta=0.9, verbose=False, seed=0, multi_targeted=False, n_classes=10)
    elif attacker_name == 'AutoAttack':
        attacker = torchattacks.AutoAttack(model, norm='Linf', eps=8/255, version='standard', n_classes=10, seed=None, verbose=False)
    elif attacker_name == 'Square':
        attacker = torchattacks.Square(model, norm='Linf', eps=8/255, n_queries=5000, n_restarts=1, p_init=.8, seed=0, verbose=False, loss='margin', resc_schedule=True)
    elif attacker_name == 'SPSA':
        attacker = torchattacks.SPSA(model, eps=0.3)
    elif attacker_name == 'JSMA':
        attacker = torchattacks.JSMA(model, theta=1.0, gamma=0.1)
    elif attacker_name == 'EADL1':
        attacker = torchattacks.EADL1(model, kappa=0, lr=0.01, max_iterations=100)
    elif attacker_name == 'EADEN':
        attacker = torchattacks.EADEN(model, kappa=0, lr=0.01, max_iterations=100)
    elif attacker_name == 'PIFGSM':
        attacker = torchattacks.PIFGSM(model, max_epsilon=16 / 255, num_iter_set=10, momentum=1.0, amplification=10.0, prob=0.7)
    elif attacker_name == 'PIFGSMPP':
        attacker = torchattacks.PIFGSMPP(model, max_epsilon=16 / 255, num_iter_set=10, momentum=1.0, amplification=10.0, prob=0.7, project_factor=0.8)

    attacker.set_normalization_used(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    return attacker




