# import tensorflow as tf
import numpy as np
import model
import input_data
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


def get_one_image(img_list):
    """
        Inputs:
            img_list: List of image paths
        Returns:
            image: A randomly selected image from the list of image paths
    """
    n = len(img_list)                  # Get the total number of images in the folder
    ind = np.random.randint(0, n)      # Randomly select an index from 0 to n
    # Get the image path based on the random index
    img_dir = img_list[ind]

    image = Image.open(img_dir)        # Open the image at img_dir
    image = image.resize([208, 208])   # Resize the image to 208x208 pixels
    # Convert the image to a multi-dimensional array
    image = np.array(image)
    return image


def evaluate_one_image():
    # Change to your own test dataset directory
    test_dir = 'D:/WorkSpace/work_to_pycharm/cats_vs_dogs/data/test/'
    # test_dir = '/home/user/Dataset/cats_vs_dogs/test/'

    # Get the list of test image paths
    test_img = input_data.get_files(test_dir)[0]
    # Randomly select an image from the test dataset
    image_array = get_one_image(test_img)

    # Set this graph as the default graph. This session will also be the default session.
    with tf.Graph().as_default():    # Reference: https://blog.csdn.net/nanhuaibeian/article/details/101862790
        # We are inputting one image (predicting this random image)
        BATCH_SIZE = 1
        N_CLASSES = 2                # Binary classification (cat or dog)

        # Convert the array to a format recognized by TensorFlow
        image = tf.cast(image_array, tf.float32)
        image = tf.image.per_image_standardization(
            image)           # Standardize the image
        # Reshape the image
        image = tf.reshape(image, [1, 208, 208, 3])
        # Get the prediction from the neural network output layer
        logit = model.cnn_inference(image, BATCH_SIZE, N_CLASSES)
        # Apply softmax to get probabilities summing to 1
        logit = tf.nn.softmax(logit)

        # Placeholder for input data with the defined shape
        x = tf.placeholder(tf.float32, shape=[208, 208, 3])

        # Change to your own trained model path
        logs_train_dir = 'D:/WorkSpace/work_to_pycharm/cats_vs_dogs/log/'

        saver = tf.train.Saver()

        with tf.Session() as sess:
            print("Loading model from specified path...")
            # Read the checkpoint from the path
            ckpt = tf.train.get_checkpoint_state(logs_train_dir)
            # Load the model, no need to provide the model name, the checkpoint file will locate the latest saved model
            if ckpt and ckpt.model_checkpoint_path:                # If checkpoint exists and contains variables
                global_step = ckpt.model_checkpoint_path.split(
                    '/')[-1].split('-')[-1]   # Extract global step from the checkpoint
                # Restore all parameters from the path into the current session
                saver.restore(sess, ckpt.model_checkpoint_path)
                print('Model loaded successfully, trained for %s steps' %
                      global_step)
            else:
                print('Model loading failed, checkpoint file not found!')

            # Restore the trained model parameters (i.e., weights in the neural network) with saver.restore()
            # Execute sess.run() to run and return the result data
            # Input the randomly selected image data to get the prediction
            prediction = sess.run(logit, feed_dict={x: image_array})
            # Get the index of the highest probability in the output
            max_index = np.argmax(prediction)
            if max_index == 0:
                pre = prediction[:, 0][0] * 100
                # If index is 0, it's a cat, print the probability
                print(
                    'The probability that the image is a cat: {:.2f}%'.format(pre))
            else:
                pre = prediction[:, 1][0] * 100
                # If index is 1, it's a dog, print the probability
                print(
                    'The probability that the image is a dog: {:.2f}%'.format(pre))

    plt.imshow(image_array)    # Process the image
    plt.show()                 # Display the image


if __name__ == '__main__':
    # Call the method to start testing
    evaluate_one_image()
