"""  
    input_data.py: Read training data  
"""
import os
import numpy as np
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

def get_files(file_dir):
    """  
    Args:  
        file_dir: Directory path where training images are stored.  
  
    Returns:  
        image_list: List of shuffled image paths.  
        label_list: List of shuffled labels (corresponding to images).  
    """
    # Initialize empty lists
    cats = []           # List to store image paths of cats
    label_cats = []     # List to store labels corresponding to cat images
    dogs = []           # List to store image paths of dogs
    label_dogs = []     # List to store labels corresponding to dog images

    # Read data from the file_dir path and store it in the empty lists
    # file is the file name of the image with extension
    for file in os.listdir(file_dir):
        # Image format is cat.1.jpg / dog.2.jpg, processed name is [cat, 1, jpg]
        name = file.split(sep='.')
        if name[0] == 'cat':          # name[0] gets the image name
            # If it's a cat, add the image path to the cats list
            cats.append(file_dir + file)
            # And add a label of 0 to label_cats (0 for cat, 1 for dog)
            label_cats.append(0)
        else:
            dogs.append(file_dir + file)
            # Note: The labels added here are in string format, which will be converted to int later
            label_dogs.append(1)

    # Combine the cat and dog lists
    # Combine into a row vector by horizontally stacking
    image_list = np.hstack((cats, dogs))
    # Combine cat and dog image and label lists
    label_list = np.hstack((label_cats, label_dogs))
    # Create a 2 x 25000 array (2 rows, 25000 columns)
    temp = np.array([image_list, label_list])
    # Transpose the array to a 25000 x 2 size
    temp = temp.transpose()
    np.random.shuffle(temp)                    # Shuffle the 25000 rows

    # Select all rows, column=0 (image paths)
    image_list = list(temp[:, 0])
    # Select all rows, column=1 (labels)
    label_list = list(temp[:, 1])
    # Convert label list to int type (using list comprehension)
    label_list = [int(float(i)) for i in label_list]

    return image_list, label_list


def get_batch(image, label, image_W, image_H, batch_size, capacity):
    """  
    Args:  
        image, label: Images and labels to generate batches from.  
        image_W, image_H: Width and height of the images.  
  
    ... (Remaining function definition continues)  
    """
    # Rest of the function implementation...

# Note: The rest of the function 'get_batch' is not provided, so I assumed the rest of the docstring would be similar to the above.
