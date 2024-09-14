
import matplotlib.pyplot as plt
import datetime
import os
import torch


def main():
	show_pic = False # show plots or not.

	current_date = datetime.datetime.now()
	date_str = current_date.strftime("%Y-%m-%d-%H") # Convert the date to a string in the "YYYY-MM-DD-HH" format

	model_list = ['WideResNet']
	dataset_list = ['cifar10'] #', 'cifar100', 'mnist']
	attack_list = ['PGD','FGSM']#, 'CW','BIM','PGDL2', 'Jitter', 'VMIFGSM', 'NIFGSM']
	'''attack_list = ['VANILA', 'GN', 'FGSM', 'BIM', 'RFGSM', 'PGD', 'EOTPGD', \
	                            'FFGSM', 'TPGD', 'MIFGSM', 'UPGD', 'APGD', 'APGDT', 'DIFGSM', 'TIFGSM', 'Jitter',\
	                            'NIFGSM', 'PGDRS', 'SINIFGSM', 'VMIFGSM', 'VNIFGSM', 'CW', 'PGDL2', 'PGDRSL2',\
	                            'DeepFool', 'SparseFool', 'OnePixel', 'Pixle', 'FAB', 'AutoAttack', 'Square',\
	                            'SPSA', 'JSMA', 'EADL1', 'EADEN', 'PIFGSM', 'PIFGSMPP']'''
	detector_list = ["ReAct", "OpenMax", "TemperatureScaling", "KNN", 'ODIN', 'EnergyBased', 'Entropy', 'KLMatching', 'Mahalanobis',\
	'Mahalanobis+ODIN', 'MaxLogit','ViM', 'RMD', 'DICE', 'SHE', "MSP", "MCD", "ASH"]
	print(date_str)

	saved_directory_path = './output/process_result/'
	if not os.path.exists(saved_directory_path):
		os.makedirs(saved_directory_path)
	

	# data_dict['originalROC'] = p, r
    # data_dict['original_scores'] = (in_scores, out_scores)
    # data_dict['modified_scores'] = (in_scores, out_scores)
    # data_dict['modifiedROC'] = p, r
    # data_dict['data'] = metrics.compute()

	
    # file_name = os.path.join(directory_path, '{}_{}_{}.pt'.format(detector_name, attack_name, dataset_name))

	originalROC = {}
	modifiedROC = {}
	original_scores = {}
	modified_scores = {}

	for dataset in dataset_list:
		for attack in attack_list:
			for detector in detector_list:
			    data_dict = torch.load('./output/detector_result/{}_{}_{}.pt'.format(detector,attack,dataset))
			    originalROC[detector,attack] = data_dict['originalROC']
			    modifiedROC[detector,attack] = data_dict['modifiedROC']
			    original_scores[detector,attack] = data_dict['original_scores']
			    modified_scores[detector,attack] = data_dict['modified_scores']

    print('data loaded')

	fig,ax = plt.subplots(nrows=max(2,len(attack_list)),ncols=len(detector_list),
                      figsize=(6*len(detector_list),  6*len(attack_list)))
	#,sharex=True,figsize=(6,7) gridspec_kw={'width_ratios': [len(detectors)*len(attackers)]*2
	for ida,attack_name in enumerate(attack_list):
	    for idd, detector_name in enumerate(detector_list):
	        scores_in, scores_out = modified_scores[detector_name, attack_name]
	        ax[ida,idd].hist(scores_in, histtype='step', label='scores of in distribution')
	        ax[ida,idd].hist(scores_out, histtype='step', label='scores of out of distribution')
	        ax[ida,idd].set_title(detector_name +'&'+ attack_name )
	    ax[ida,idd].legend(loc='center left', bbox_to_anchor=(1, 0.5))
	fig.tight_layout()
	if show_pic:
		plt.show()
	fig.savefig(saved_directory_path+'Modified Hist of ID and OOD scores '+date_str+'.png')

	# Plot original Hist
	fig,ax = plt.subplots(nrows=max(2,len(attack_list)),ncols=len(detector_list),
	                      figsize=(6*len(detector_list),  6*len(attack_list)))
	#,sharex=True,figsize=(6,7) gridspec_kw={'width_ratios': [len(detectors)*len(attackers)]*2
	for ida,attack_name in enumerate(attack_list):
	    for idd, detector_name in enumerate(detector_list):
	        scores_in, scores_out = original_scores[detector_name, attack_name]
	        ax[ida,idd].hist(scores_in, histtype='step', label='scores of in distribution')
	        ax[ida,idd].hist(scores_out, histtype='step', label='scores of out of distribution')
	        ax[ida,idd].set_title(detector_name +'&'+ attack_name )
	    ax[ida,idd].legend(loc='center left', bbox_to_anchor=(1, 0.5))
	fig.tight_layout()
	if show_pic:
		plt.show()
	fig.savefig(saved_directory_path + 'Original Hist of ID and OOD scores '+date_str+'.png')


	fig,ax = plt.subplots(len(attack_list),1,figsize=(6, max(6,3*len(attack_list))))
	for i, attack_name in enumerate(attack_list):
	    for detector_name in detector_list:
	        p,r = modifiedROC[detector_name,attack_name]
	        ax[i].plot(p,r,label=detector_name)
	    ax[i].set_title('ROC Curves under Attack: ' + attack_name)
	    ax[i].legend(loc='center left', bbox_to_anchor=(1, 0.5))
	fig.tight_layout()
	if show_pic:
		plt.show()
	fig.savefig(saved_directory_path + 'Modified ROC curves '+date_str+'.png')

	fig,ax = plt.subplots(len(attack_list),1,figsize=(6, max(6,3*len(attack_list))))
	for i, attack_name in enumerate(attack_list):
	    for detector_name in detector_list:
	        p,r = originalROC[detector_name,attack_name]
	        ax[i].plot(p,r,label=detector_name)
	    ax[i].set_title('ROC Curves under Attack: ' + attack_name)
	    ax[i].legend(loc='center left', bbox_to_anchor=(1, 0.5))
	fig.tight_layout()
	if show_pic:
		plt.show()
	fig.savefig(saved_directory_path + 'Original ROC curves '+date_str+'.png')


if __name__ == '__main__':
    main()
