"""
    model.py: CNN neural network model
"""
# import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


def cnn_inference(images, batch_size, n_classes):
    """
        Inputs:
            images: A batch of images from the queue, specifically a 4D tensor [batch_size, width, height, 3]
            batch_size: The size of each batch
            n_classes: The number of classes (here it's binary classification, cat or dog)
        Returns:
            softmax_linear: The predicted probabilities of each image in the batch being either a cat or a dog 
                            (i.e., the output values computed by the neural network).
                            For example: [[0.459, 0.541], ..., [0.892, 0.108]],
                            One value represents the probability of being a cat, the other represents the probability of being a dog, and their sum is 1.
    """

    # TensorFlow variable scope mechanism:
    #       tf.variable_scope(<scope_name>): Specify a namespace
    #       tf.get_variable(<name>, <shape>, <dtype>, <initializer>): Create a variable

    # First convolutional layer conv1, the size of the kernel (weights) is 3*3, the input channel is 3, and there are 16 of them
    with tf.variable_scope('conv1') as scope:
        # tf.truncated_normal_initializer(): weights initialized with truncated normal distribution, stddev is standard deviation
        weights = tf.get_variable('weights',
                                  shape=[3, 3, 3, 16],
                                  dtype=tf.float32,
                                  initializer=tf.truncated_normal_initializer(stddev=0.1, dtype=tf.float32))
        biases = tf.get_variable('biases',
                                 shape=[16],
                                 dtype=tf.float32,
                                 initializer=tf.constant_initializer(0.1))  # Initialized to a constant, usually the biases are initialized this way

        # strides = [1, y_movement, x_movement, 1], the stride of the sliding window for each dimension, generally fixed to 1 at the beginning and end
        # padding = 'SAME', consider the boundary, use 0 to pad around if insufficient
        # padding = 'VALID', do not consider the boundary, discard if insufficient, do not pad around
        # Input images are [16, 208, 208, 3], i.e., 16 images of size 208*208, with 3 channels
        # weights (kernels) are of size 3*3, and there are 16 of them
        # strides (stride length) is [1, 1, 1, 1], i.e., the kernel moves 1 unit in the x and y directions when convolving over the image
        # With padding='SAME' considering boundaries, the result is 16 images each producing 16 feature maps of 208*208
        # conv (final output) is a 4D tensor of shape [16, 208, 208, 16]
        # Convolve images with weights
        conv = tf.nn.conv2d(images, weights, strides=[
                            1, 1, 1, 1], padding='SAME')
        # Add biases, biases vector is added to each row of the matrix, shape remains unchanged
        pre_activation = tf.nn.bias_add(conv, biases)
        # Use ReLU activation function for non-linear processing in the conv1 namespace
        conv1 = tf.nn.relu(pre_activation, name='conv1')

    # First pooling layer pool1 and normalization norm1 (feature scaling)
    with tf.variable_scope('pooling1_lrn') as scope:
        # Pool the feature map from conv1
        pool1 = tf.nn.max_pool(conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                               padding='SAME', name='pooling1')
        # lrn(): Local response normalization, a method to prevent overfitting, enhances the model's generalization ability
        norm1 = tf.nn.lrn(pool1, depth_radius=4, bias=1.0, alpha=0.001/9.0,
                          beta=0.75, name='norm1')

    # Second convolutional layer conv2, the size of the kernel (weights) is 3*3, the input channel is 16, and there are 16 of them
    with tf.variable_scope('conv2') as scope:
        weights = tf.get_variable('weights',
                                  # The third number here needs to equal the dimension of the tensor from the previous layer
                                  shape=[3, 3, 16, 16],
                                  dtype=tf.float32,
                                  initializer=tf.truncated_normal_initializer(stddev=0.1, dtype=tf.float32))
        biases = tf.get_variable('biases',
                                 shape=[16],
                                 dtype=tf.float32,
                                 initializer=tf.constant_initializer(0.1))
        conv = tf.nn.conv2d(norm1, weights, strides=[
                            1, 1, 1, 1], padding='SAME')
        pre_activation = tf.nn.bias_add(conv, biases)
        conv2 = tf.nn.relu(pre_activation, name='conv2')

    # Second pooling layer pool2 and normalization norm2 (feature scaling)
    with tf.variable_scope('pooling2_lrn') as scope:
        # Here, normalization is done before pooling
        norm2 = tf.nn.lrn(conv2, depth_radius=4, bias=1.0, alpha=0.001/9.0,
                          beta=0.75, name='norm2')
        pool2 = tf.nn.max_pool(norm2, ksize=[1, 2, 2, 1], strides=[1, 1, 1, 1],
                               padding='SAME', name='pooling2')

    # Third layer is fully connected layer local3
    # Connect all features and pass the output to the classifier (map features to sample label space), this layer maps 256 outputs
    with tf.variable_scope('local3') as scope:
        # Flatten pool2 tensor, then adjust the dimension to shape (the -1 in shape will be automatically calculated during runtime)
        reshape = tf.reshape(pool2, shape=[batch_size, -1])

        # Get the number of columns after reshaping
        dim = reshape.get_shape()[1].value
        weights = tf.get_variable('weights',
                                  shape=[dim, 256],  # Connect 256 neurons
                                  dtype=tf.float32,
                                  initializer=tf.truncated_normal_initializer(stddev=0.005, dtype=tf.float32))
        biases = tf.get_variable('biases',
                                 shape=[256],
                                 dtype=tf.float32,
                                 initializer=tf.constant_initializer(0.1))
        # Multiply matrices and add biases, use ReLU activation function for non-linear processing
        local3 = tf.nn.relu(tf.matmul(reshape, weights) +
                            biases, name='local3')

    # Fourth layer is fully connected layer local4
    # Connect all features and pass the output to the classifier (map features to sample label space), this layer maps 512 outputs
    with tf.variable_scope('local4') as scope:
        weights = tf.get_variable('weights',
                                  # Connect another 512 neurons
                                  shape=[256, 512],
                                  dtype=tf.float32,
                                  initializer=tf.truncated_normal_initializer(stddev=0.005, dtype=tf.float32))
        biases = tf.get_variable('biases',
                                 shape=[512],
                                 dtype=tf.float32,
                                 initializer=tf.constant_initializer(0.1))
        # Multiply matrices and add biases, use ReLU activation function for non-linear processing
        local4 = tf.nn.relu(tf.matmul(local3, weights) + biases, name='local4')

    # Fifth layer is the output layer (regression layer): softmax_linear
    # The output from the previous fully connected layer is linearly regressed to compute the scores for each class, here there are 2 classes, so this layer outputs two scores.
    with tf.variable_scope('softmax_linear') as scope:
        weights = tf.get_variable('weights',
                                  shape=[512, n_classes],
                                  dtype=tf.float32,
                                  initializer=tf.truncated_normal_initializer(stddev=0.005, dtype=tf.float32))
        biases = tf.get_variable('biases',
                                 shape=[n_classes],
                                 dtype=tf.float32,
                                 initializer=tf.constant_initializer(0.1))

        # The number of rows in softmax_linear = the number of rows in local4, the number of columns = the number of columns in weights = the number of rows in biases = the number of classes
        # The softmax function is used for classification, it maps multiple neurons' outputs to the interval (0, 1), can be interpreted as probabilities
        # Here local4 is multiplied by weights, then added to biases
        softmax_linear = tf.add(
            tf.matmul(local4, weights), biases, name='softmax_linear')

    # Normalization and cross-entropy are not done here. The actual softmax function is combined with cross-entropy in the losses() function below for improved computation speed.
    # The probabilities for each image in the list being each class are returned
    return softmax_linear


def losses(logits, labels):
    """
        Inputs:
            logits: The output values from cnn_inference (the predicted probabilities for each image in the list being either a cat or a dog)
            labels: The labels corresponding to the images (i.e., the true values, used to compare with the logits to get the loss)
        Returns:
            loss: The loss value (the error between the true labels and the predicted values)
    """
    with tf.variable_scope('loss') as scope:
        cross_entropy = tf.nn.sparse_softmax_cross_entropy_with_logits(
            logits=logits, labels=labels, name='xentropy_per_example')
        loss = tf.reduce_mean(cross_entropy, name='loss')
        tf.summary.scalar(scope.name+'/loss', loss)
    return loss


def training(loss, learning_rate):
    """
        Inputs:
            loss: The loss value (the error between the true labels and the predicted values)
            learning_rate: The learning rate for the optimizer
        Returns:
            train_op: The training operation (the optimizer used to update the model's parameters)
    """
    with tf.variable_scope('optimizer') as scope:
        optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate)
        global_step = tf.Variable(0, name='global_step', trainable=False)
        train_op = optimizer.minimize(loss, global_step=global_step)
    return train_op


def evaluation(logits, labels):
    """
        Inputs:
            logits: The output values from cnn_inference (the predicted probabilities for each image in the list being either a cat or a dog)
            labels: The labels corresponding to the images (i.e., the true values, used to compare with the logits to get the loss)
        Returns:
            accuracy: The accuracy of the model (the proportion of correct predictions)
    """
    with tf.variable_scope('accuracy') as scope:
        correct = tf.nn.in_top_k(logits, labels, 1)
        correct = tf.cast(correct, tf.float16)
        accuracy = tf.reduce_mean(correct)
        tf.summary.scalar(scope.name+'/accuracy', accuracy)
    return accuracy
