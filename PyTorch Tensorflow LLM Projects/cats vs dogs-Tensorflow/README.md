## File description
* data (folder): contains test test set and train training set
* log (folder): save training model and parameters
* image (folder): stores training images and prediction result images
* input_data.py: Responsible for reading data and generating batches
* model.py: Responsible for implementing our neural network model
* training.py: responsible for implementing model training and evaluation [1. Run this first to train the model, and then run test.py]
* test.py: Randomly select a picture from the test set to predict whether it is a cat or a dog [2. After running training.py, run this again to test the picture to predict whether it is a cat or a dog]

## be careful
* The path for reading files in training.py and test.py needs to be modified to match your current folder path
* Package import problem (the code interface of this project uses tensorflow version 1. If the tensorflow installed is version 2, just import the package as follows)
```python
# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
```

## Training graph (accuracy and loss value)
(./image/Accuracy&Loss.png)

## Prediction result graph
(./image/Prediction.jpg)