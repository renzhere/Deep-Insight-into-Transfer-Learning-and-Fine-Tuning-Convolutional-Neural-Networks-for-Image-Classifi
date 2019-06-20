"""binary_classification_pre-trained.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BIOyrf0OJMfyVq4p7xAMGm29vv5ePXnt
"""

import cv2
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
# %matplotlib inline 


from google.colab import drive
drive.mount('/content/gdrive')

path =  '/content/gdrive/My Drive/keras_lab_dataset/dogs_cats/dogs_cats/data'


from keras.applications import InceptionResNetV2

conv_base = InceptionResNetV2(weights = 'imagenet', include_top = False, input_shape = (64,64,3))

from keras.applications import VGG16

conv_base_vgg16 = VGG16(weights = 'imagenet', include_top = False, input_shape = (64,64,3))

from keras.applications import ResNet50

conv_base_ResNet50 = ResNet50(weights = 'imagenet', include_top = False, input_shape = (64,64,3))

from keras.applications import InceptionV3

conv_base_InceptionV3 = InceptionV3(weights = 'imagenet', include_top = False, input_shape = (64,64,3))


def preprocess_dataset(dataDir, labelDictionary):
  x = []
  y = []
  
  
  width, height = 64, 64
  
  # list folders in directory 
  directory = os.listdir(dataDir)
  
  #for each folder (train and validation)
  for label in directory:
    
    #add class label to label dictionary
    if label not in labelDictionary:
      labelDictionary[label] = len(labelDictionary)
      
    # create full path for image directory 
    #(append absolute and image directory path)
    sourceImages = os.path.join(dataDir, label)
    images = os.listdir(sourceImages)
    
    #for each image in directory
    for image in images:
      
      #read the image from file, resize and add to a list
      full_size_image = cv2.imread(os.path.join(sourceImages, image))
      x.append(cv2.resize(full_size_image, (width, height), 
                         interpolation = cv2.INTER_CUBIC))
      
      #add the class label to y
      y.append(label)
      
  return np.array(x), np.array(y)



def read_and_process_image(list_of_images):

  #   initialise the array for image
    X = []
  #   initialise the array for label
    y = [] 
    
    for image in list_of_images:
        X.append(cv2.resize(cv2.imread(image, cv2.IMREAD_COLOR), (nrows,ncolumns), interpolation=cv2.INTER_CUBIC)) 
      
        if 'dog' in image:
            y.append(1)
        elif 'cat' in image:
            y.append(0)
    
    return X, y

X, y = read_and_process_image(train_imgs)
X = np.array(X)
y = np.array(y)


ntrain = len(X_train)
nval = len(X_val)
batch_size = 32

from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.20, random_state=2)

print("Shape of train images is:", X_train.shape)
print("Shape of validation images is:", X_val.shape)
print("Shape of labels is:", y_train.shape)
print("Shape of labels is:", y_val.shape)



from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array, load_img


model = models.Sequential()
model.add(conv_base)
model.add(layers.Flatten())
model.add(layers.Dense(256, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()


model.compile(loss='binary_crossentropy', optimizer=optimizers.RMSprop(lr=2e-5), metrics=['acc'])



# Data Augmentation step where image processing techniques like rotation_range, 
# width_shift_range, height_shift_range, shear_range, zoom_range, 
# horizontal_flip are applied on all the image instances, to generate new
# image instances to provide sufficiently large dataset for model training

train_datagen = ImageDataGenerator(rescale=1./255,  
                                    rotation_range=40,
                                    width_shift_range=0.2,
                                    height_shift_range=0.2,
                                    shear_range=0.2,
                                    zoom_range=0.2,
                                    horizontal_flip=True,)

val_datagen = ImageDataGenerator(rescale=1./255)


train_generator = train_datagen.flow(X_train, y_train, batch_size=batch_size)
val_generator = val_datagen.flow(X_val, y_val, batch_size=batch_size)


H = model.fit_generator(train_generator,
                              steps_per_epoch=ntrain // batch_size,
                              epochs=20,
                              validation_data=val_generator,
                              validation_steps=nval // batch_size)

# store the history of training in history and its plot the graphs

import tensorflow as tf
import h5py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import os

from glob import glob
NUM_EPOCHS = 20

plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, NUM_EPOCHS), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, NUM_EPOCHS), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, NUM_EPOCHS), H.history["acc"], label="train_acc")
plt.plot(np.arange(0, NUM_EPOCHS), H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.show()


X_test, y_test = read_and_process_image(test_imgs[0:4]) 
x = np.array(X_test)
test_datagen = ImageDataGenerator(rescale=1./255)

# predict on first 4 images in the test set and plot the results
i = 0
text_labels = []
plt.figure(figsize=(30,20))
for batch in test_datagen.flow(x, batch_size=1):
    pred = model.predict(batch)
    if pred > 0.5:
        text_labels.append('dog')
    else:
        text_labels.append('cat')
    plt.subplot(5 / columns + 1, columns, i + 1)
    plt.title(text_labels[i])
    imgplot = plt.imshow(batch[0])
    i += 1
    if i % 10 == 0:
        break
plt.show()

model_vgg = models.Sequential()
model_vgg.add(conv_base_vgg16)
model_vgg.add(layers.Flatten())
model_vgg.add(layers.Dense(256, activation='relu'))
model_vgg.add(layers.Dense(1, activation='sigmoid'))

# model_vgg.summary()

print('Number of trainable weights :', len(model.trainable_weights))
conv_base_vgg16.trainable = False
print('Number of trainable weights after freezing base:', len(model.trainable_weights))

model_vgg.compile(loss='binary_crossentropy', optimizer=optimizers.RMSprop(lr=2e-5), metrics=['acc'])

H_vgg = model_vgg.fit_generator(train_generator,
                              steps_per_epoch=ntrain // batch_size,
                              epochs=20,
                              validation_data=val_generator,
                              validation_steps=nval // batch_size)


import tensorflow as tf
import h5py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import os

from glob import glob
NUM_EPOCHS = 20

plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, NUM_EPOCHS), H_vgg.history["loss"], label="train_loss")
plt.plot(np.arange(0, NUM_EPOCHS), H_vgg.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, NUM_EPOCHS), H_vgg.history["acc"], label="train_acc")
plt.plot(np.arange(0, NUM_EPOCHS), H_vgg.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.show()

model_ResNet = models.Sequential()
model_ResNet.add(conv_base_ResNet50)
model_ResNet.add(layers.Flatten())
model_ResNet.add(layers.Dense(256, activation='relu'))
model_ResNet.add(layers.Dense(1, activation='sigmoid'))

# model_vgg.summary()

print('Number of trainable weights :', len(model.trainable_weights))
conv_base_ResNet50.trainable = False
print('Number of trainable weights after freezing  base:', len(model.trainable_weights))

model_ResNet.compile(loss='binary_crossentropy', optimizer=optimizers.RMSprop(lr=2e-5), metrics=['acc'])

H_ResNet = model_ResNet.fit_generator(train_generator,
                              steps_per_epoch=ntrain // batch_size,
                              epochs=20,
                              validation_data=val_generator,
                              validation_steps=nval // batch_size)


import tensorflow as tf
import h5py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import os

from glob import glob
NUM_EPOCHS = 20

plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, NUM_EPOCHS), H_ResNet.history["loss"], label="train_loss")
plt.plot(np.arange(0, NUM_EPOCHS), H_ResNet.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, NUM_EPOCHS), H_ResNet.history["acc"], label="train_acc")
plt.plot(np.arange(0, NUM_EPOCHS), H_ResNet.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.show()

model_InceptionV3 = models.Sequential()
model_InceptionV3.add(conv_base_InceptionV3)
model_InceptionV3.add(layers.Flatten())
model_InceptionV3.add(layers.Dense(256, activation='relu'))
model_InceptionV3.add(layers.Dense(1, activation='sigmoid'))

print('Number of trainable weights :', len(model.trainable_weights))
conv_base_InceptionV3.trainable = False
print('Number of trainable weights after freezing base:', len(model.trainable_weights))

model_InceptionV3.compile(loss='binary_crossentropy', optimizer=optimizers.RMSprop(lr=2e-5), metrics=['acc'])

H_IV3 = model_InceptionV3.fit_generator(train_generator,
                              steps_per_epoch=ntrain // batch_size,
                              epochs=20,
                              validation_data=val_generator,
                              validation_steps=nval // batch_size)


import tensorflow as tf
import h5py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2
import os

from glob import glob
NUM_EPOCHS = 20

plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, NUM_EPOCHS), H_IV3.history["loss"], label="train_loss")
plt.plot(np.arange(0, NUM_EPOCHS), H_IV3.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, NUM_EPOCHS), H_IV3.history["acc"], label="train_acc")
plt.plot(np.arange(0, NUM_EPOCHS), H_IV3.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.show()