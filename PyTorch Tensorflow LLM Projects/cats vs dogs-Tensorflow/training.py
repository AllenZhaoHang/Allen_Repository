# import tensorflow as tf
import model
import input_data
import matplotlib.pyplot as plt
import numpy as np
import os
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()


N_CLASSES = 2  # Number of classes, cat and dog
IMG_W = 208  # Resize image width and height, too large will result in long training time
IMG_H = 208
BATCH_SIZE = 16  # Number of data read per batch
CAPACITY = 2000  # Maximum queue capacity
MAX_STEP = 10000  # Maximum training steps, generally between 5K and 10K
learning_rate = 0.0001  # Learning rate, generally less than 0.0001

# train_dir = 'D:/WorkSpace/Dataset/cats_vs_dogs/data/train/'        # Path to the training dataset folder
# logs_train_dir = 'D:/WorkSpace/work_to_pycharm/cats_vs_dogs/log/'  # Path to log the training process and save the model
# Path to the training dataset folder
train_dir = '/home/user/Dataset/cats_vs_dogs/train/'
# Path to log the training process and save the model
logs_train_dir = '/home/dujunjie/PycharmProjects/cats_vs_dogs/log/'

# Get the images to be trained and their corresponding labels. The returned train_img is a list of cat and dog image paths, and train_label is a list of corresponding labels (0 for cat, 1 for dog).
train_img, train_label = input_data.get_files(train_dir)

# Read data from the queue
train_batch, train_label_batch = input_data.get_batch(
    train_img, train_label, IMG_W, IMG_H, BATCH_SIZE, CAPACITY)

# Call model methods to get return values and assign variables
train_logits = model.cnn_inference(train_batch, BATCH_SIZE, N_CLASSES)
train_loss = model.losses(train_logits, train_label_batch)
train_op = model.training(train_loss, learning_rate)
train_acc = model.evaluation(train_logits, train_label_batch)

# Save all summaries to disk for tensorboard display
summary_op = tf.summary.merge_all()

accuracy_list = []   # Record accuracy (saved every 50 steps)
loss_list = []       # Record loss value (saved every 50 steps)
step_list = []       # Record training steps (saved every 50 steps)


with tf.Session() as sess:
    # Variable initialization, essential if variables exist
    sess.run(tf.global_variables_initializer())

    # Write summary (training) to logs_train_dir
    train_writer = tf.summary.FileWriter(logs_train_dir, sess.graph)
    # Used to save the trained model
    saver = tf.train.Saver()

    # Queue monitoring (batch data in training uses a queue)
    coord = tf.train.Coordinator()   # Create thread coordinator
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    try:
        # Execute training for MAX_STEP steps, one batch at a time
        for step in np.arange(MAX_STEP):
            if coord.should_stop():   # Stop training if all data in the queue has been read
                break

            # Read TensorFlow variable values in the session
            _op, tra_loss, tra_acc = sess.run(
                [train_op, train_loss, train_acc])

            # Print current loss and accuracy every 50 steps, and log, save to writer
            if step % 50 == 0:
                print('Step %d, train loss = %.2f, train accuracy = %.2f%%' %
                      (step, tra_loss, tra_acc * 100.0))
                # Call sess.run(), generate training data
                summary_train = sess.run(summary_op)
                # Save training process and training steps
                train_writer.add_summary(summary_train, step)

            # Plot and record training accuracy and loss values every 100 steps
            if step % 100 == 0:
                accuracy_list.append(tra_acc)
                loss_list.append(tra_loss)
                step_list.append(step)

            # Save the trained model every 5000 steps (i.e., save the parameters of the trained model)
            if step % 5000 == 0 or (step + 1) == MAX_STEP:
                # ckpt file is a binary file that maps variable names to corresponding tensor values
                checkpoint_path = os.path.join(logs_train_dir, 'model.ckpt')
                saver.save(sess, checkpoint_path, global_step=step)

        plt.figure()                    # Establish a visual image frame
        # Blue line for accuracy
        plt.plot(step_list, accuracy_list, color='b', label='cnn_accuracy')
        plt.plot(step_list, loss_list, color='r', label='cnn_loss',
                 linestyle='dashed')   # Red dashed line for loss value
        plt.xlabel("Step")              # Name x-axis
        plt.ylabel("Accuracy/Loss")     # Name y-axis
        plt.legend()                    # Add legend to the graph
        plt.show()                      # Display image

    except tf.errors.OutOfRangeError:
        print('Done training -- epoch limit reached')
    finally:
        coord.request_stop()   # Stop all threads

    coord.join(threads)   # Wait for all threads to end
    sess.close()          # Close session
