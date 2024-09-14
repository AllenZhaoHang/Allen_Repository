# OOD Research Pipe
I am still working on it...

## Instructions
  use `make_gen_att.sh` to generate run script
  
  use `submit.sh` to run in MSI

## Examples
  - Generate run scrip
      ```ruby
      bash make_gen_att.sh
      ```

  - Generate CIFAR10 data under FGSM attack:
      ```ruby
      python generate_attack_data.py --attack_name FGSM --dataset cifar10
      ```

  - Evaluate Mahalanobis detector under PGD attack
      ```ruby
      python detectors_eval.py --model WideResNet --attack_data PGD_cifar10 --detector Mahalanobis
      ```

## Code Explanations

	1. **attacker_maker.py**

	This code defines a function `make_attacker` used to create different types of adversarial attackers. These attackers are tools designed to generate adversarial samples, which can be used to test and improve the robustness of machine learning models. Adversarial attacks are typically used to detect vulnerabilities in models, specifically whether a model’s output changes significantly with small changes to the input.

	**make_attacker Function**
	**Parameters:**
	- `attacker_name`: A string indicating the name of the attacker.
	- `model`: The machine learning model to be subjected to adversarial attacks.

	**Functionality:** Based on the provided attacker name and model, it creates and returns the corresponding attacker instance.

	2. **clear.sh**
	File deletion script.

	3. **dataset_maker.py**

	Loads the corresponding dataset based on the specified dataset name, preprocesses the data, and then returns the training and testing DataLoaders. A DataLoader is a tool in PyTorch responsible for loading data in batches during training.

	4. **detector_maker.py**

	This code primarily creates different types of Out-Of-Distribution (OOD) detectors and trains them. It involves defining and using several OOD detector models and includes the basic steps of data loading and preprocessing.

	5. **detectors_eval.py**

	The main purpose of this code is to generate a neural network model, load attack datasets, use different detectors to detect attacks, evaluate the performance of the detectors, and finally save the detection results. These functions combine elements from PyTorch, TorchMetrics, and custom modules.

	**Code Structure Overview**
	- Import dependencies
	- Parse parameters
	- Main functional functions
	- Main function

	6. **detectors_eval_base_1.sh**

	This Bash script is primarily used to batch evaluate the performance of different detectors on different attack datasets. It uses several command-line tools and Python scripts to speed up the evaluation process by executing multiple tasks in parallel. Below is a detailed explanation of the code.

	**Script Structure**
	- Data preparation
	- Batch evaluation of detectors
	- Use `wait` to manage parallel processes

	7. **dir_prep.py**

	This code is a Python script used for setting up file directories and downloading datasets. The main functions include:
	- Creating the necessary folders.
	- Downloading and processing the CIFAR-10 dataset.

	8. **generate_attack_data.py**

	The function of this code is to generate a dataset with adversarial attacks and save it as a file. It includes the following main steps:
	- Setting up directory structures.
	- Parsing command-line parameters.
	- Generating the model.
	- Creating adversarial attackers.
	- Performing adversarial attacks on training and testing data.
	- Saving the generated dataset.

	9. **generate_attack_data_base_1.sh**

	This Bash script is used to generate adversarial samples. It utilizes the Python script `generate_attack_data.py` to generate different types of adversarial attack data, specifically targeting the CIFAR-10 dataset. The script specifies the GPU for each Python process using the `CUDA_VISIBLE_DEVICES` environment variable to execute multiple adversarial sample generation tasks in parallel. After each batch is completed, the script waits for all processes to finish before proceeding to the next batch.

	10. **generate_attack_data_longtime.sh**

	This Bash script is used to generate adversarial samples targeting the CIFAR-10 dataset using different adversarial attack methods.

	11. **job_describe.sh**

	The purpose of this Bash script is to run the Python script `generate_attack_data.py` in an HPC (High-Performance Computing) environment and redirect the output to a file named `result`.

	12. **make_dec_eval.sh**

	The purpose of this Bash script is to execute a Python script `make_scripts_to_eval_detectors.py` and pass some parameters to it.

	13. **make_gen_att.sh**

	The purpose of this script is to call the Python script `make_scripts.py` through Bash and pass several parameters to it. These parameters may influence how the script is executed, such as specifying the task to perform (`generate_attack_data`), the mode to execute in (`base`), the number of iterations (4), the starting GPU device number (0), and the number of available GPUs (4). The specific operation and effect depend on how the `make_scripts.py` script is implemented and interprets these parameters.

	14. **make_scripts.py**

	The primary purpose of this code is to generate Bash scripts that execute multiple combinations of attacks and datasets in parallel based on the given parameters. It uses a command-line argument parser `argparse` to parse the input parameters, generates corresponding control parameter combinations based on different modes, and generates multiple Bash script files containing parallel execution commands.

	15. **make_scripts_to_eval_detectors.py**

	The primary purpose of this code is to generate Bash scripts that evaluate multiple combinations of models, datasets, attacks, and detectors in parallel based on the given parameters. It uses a command-line argument parser `argparse` to parse the input parameters, generates corresponding control parameter combinations based on different modes, and generates multiple Bash script files containing parallel execution commands.

	16. **model_maker.py**

	The purpose of this code is to create the corresponding WideResNet model based on the input model name and move it to the specified device (default is the first GPU). This design allows users to easily create and configure different model objects and perform calculations on a GPU or CPU as needed.

	17. **process_results.py**

	This code loads the precomputed results of detectors under different datasets and attacks and uses the `matplotlib` library to plot modified and original ID and OOD score histograms as well as ROC curves. Each chart title and legend clearly display the performance of different detectors under various conditions.

	18. **results.txt**
	Output log.

	19. **submit.sh**

	The purpose of this script is to configure the environment and resources in a high-performance computing environment and submit a Bash script named `generate_attack_data_base_1.sh` to execute the task of generating attack data, while saving the output to a `result` file.

