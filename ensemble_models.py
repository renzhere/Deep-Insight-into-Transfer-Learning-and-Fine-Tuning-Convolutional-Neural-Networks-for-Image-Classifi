from google.colab import drive
drive.mount('/content/gdrive')


"""
@author: STUDENT-CIT\r00171231
"""

import tensorflow as tf

import os
import numpy as np
from PIL import Image
import numpy as np

from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.layers import Dense, Activation, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D


def model_M1():
    input_shape = (32, 32, 3)
     #single convolutional layer followed by a pooling layer
    model = Sequential()
    
    model.add(Conv2D(16, (5, 5), padding = "same", input_shape = input_shape, activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Conv2D(16, (3, 3), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Conv2D(32, (3, 3), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    return model

def model_M2():
    input_shape = (32, 32, 3)
    model = Sequential()
    
    model.add(Conv2D(32, (5, 5), padding = "same", input_shape = input_shape, activation = 'relu'))
    model.add(Conv2D(32, (5, 5), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Conv2D(64, (3, 3), padding = "same", activation = 'relu'))
    model.add(Conv2D(64, (3, 3), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    return model
   
  
def model_M3():
    input_shape = (32, 32, 3)
    model = Sequential()
    
    model.add(Conv2D(32, (5, 5), padding = "same", input_shape = input_shape, activation = 'relu'))
    model.add(Conv2D(32, (5, 5), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Conv2D(64, (5, 5), padding = "same", activation = 'relu'))
    model.add(Conv2D(64, (5, 5), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Conv2D(128, (3, 3), padding = "same", activation = 'relu'))
    model.add(Conv2D(128, (3, 3), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    return model
  
  
def model_M4():
    input_shape = (32, 32, 3)
    model = Sequential()
    
    model.add(Conv2D(32, (5, 5), padding = "same", input_shape = input_shape, activation = 'relu'))
    model.add(Conv2D(32, (5, 5), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Conv2D(64, (5, 5), padding = "same", activation = 'relu'))
    model.add(Conv2D(64, (5, 5), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Conv2D(64, (3, 3), padding = "same", activation = 'relu'))
    model.add(Conv2D(128, (3, 3), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(256, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    return model
  


def model_M5():
    input_shape = (32, 32, 3)
    model = Sequential()
    
    model.add(Conv2D(32, (3, 3), padding = "same", input_shape = input_shape, activation = 'relu'))
    model.add(Conv2D(32, (3, 3), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Conv2D(64, (3, 3), padding = "same", activation = 'relu'))
    model.add(Conv2D(64, (3, 3), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    return model
  
  
def model_M6():
    input_shape = (32, 32, 3)
    model = Sequential()
    
    model.add(Conv2D(64, (3, 3), padding = "same", input_shape = input_shape, activation = 'relu'))
    model.add(Conv2D(64, (3, 3), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Conv2D(128, (3, 3), padding = "same", activation = 'relu'))
    model.add(Conv2D(128, (3, 3), padding = "same", activation = 'relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(1024, activation='relu'))
    model.add(Dense(10, activation='softmax'))

    return model

   
print("Compiling model...")
opt = tf.keras.optimizers.SGD(lr=0.01)
model1 = model_M1()
model2 = model_M2()
model3 = model_M3()
model4 = model_M4()
model5 = model_M5()
model6 = model_M6()
model1.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
model2.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
model3.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
model4.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
model5.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
model6.compile(loss="sparse_categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
 
print (model1.summary())
print (model2.summary())
print (model3.summary())
print (model4.summary())
print (model5.summary())
print (model6.summary())

# Ensemble for multi-class dataset

((trainX, trainY), (testX, testY)) = tf.keras.datasets.cifar10.load_data()
print('shape of input:', trainX.shape)
  
#   trainX=trainX.reshape(trainX[0], 64, NUM_EPOCHS64, 3)
  
  
NUM_EPOCHS = 20
#     ((trainX, trainY), (testX, testY)) = tf.keras.datasets.cifar10.load_data()
trainX = trainX.astype("float") / 255.0
testX = testX.astype("float") / 255.0
    
opt = tf.keras.optimizers.SGD(lr=0.01)
output_model_list = []

# m1=keras_model(128, 128, 3)


model1.fit(trainX, trainY, epochs=20)
val = model1.predict(testX)
output_model_list.append(val)

model2.fit(trainX, trainY, epochs=20)
val = model2.predict(testX)
output_model_list.append(val)

model3.fit(trainX, trainY, epochs=20)
val = model3.predict(testX)
output_model_list.append(val)

model4.fit(trainX, trainY, epochs=20)
val = model4.predict(testX)
output_model_list.append(val)

model5.fit(trainX, trainY, epochs=20)
val = model5.predict(testX)
output_model_list.append(val)

model6.fit(trainX, trainY, epochs=20)
val = model6.predict(testX)
output_model_list.append(val)

summed = np.sum(output_model_list, axis=0)
result = np.argmax(summed, axis=1)


from sklearn import metrics
print ( metrics.accuracy_score (result, testY))
from sklearn.metrics import classification_report
print ( metrics.classification_report (result, testY))


# Ensemble using pre-trained models
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array, load_img

from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.densenet import DenseNet121

E_model_Res = ResNet50(weights = 'imagenet', include_top = False, input_shape = (32,32,3))
E_model_Dense = DenseNet121(weights = 'imagenet', include_top = False, input_shape = (32,32,3))


print('Number of trainable weights before freezing the conv base:', len(E_model_Res.trainable_weights))
E_model_Res.trainable = False
print('Number of trainable weights after freezing the conv base:', len(E_model_Res.trainable_weights))


print('Number of trainable weights before freezing the conv base:', len(E_model_Dense.trainable_weights))
E_model_Dense.trainable = False
print('Number of trainable weights after freezing the conv base:', len(E_model_Dense.trainable_weights))


E_model1 = models.Sequential()
E_model1.add(E_model_Res)
E_model1.add(layers.Flatten())
E_model1.add(layers.Dense(256, activation='relu'))
E_model1.add(layers.Dense(10, activation='softmax'))

E_model2 = models.Sequential()
E_model2.add(E_model_Dense)
E_model2.add(layers.Flatten())
E_model2.add(layers.Dense(256, activation='relu'))
E_model2.add(layers.Dense(10, activation='softmax'))


H_Res = E_model1.compile(loss='sparse_categorical_crossentropy', optimizer=optimizers.RMSprop(lr=2e-5), metrics=['acc'])
H_Dense = E_model2.compile(loss='sparse_categorical_crossentropy', optimizer=optimizers.RMSprop(lr=2e-5), metrics=['acc'])

output_model_list2 = []

E_model1.fit(trainX, trainY, epochs=20)
val1 = E_model1.predict(testX)
output_model_list.append(val1)

E_model2.fit(trainX, trainY, epochs=20)
val2 = E_model2.predict(testX)
output_model_list.append(val2)

summed2 = np.sum(output_model_list2, axis=0)
result2 = np.argmax(summed2, axis=1)


from sklearn import metrics
print ( metrics.accuracy_score (result2, testY))
from sklearn.metrics import classification_report
print ( metrics.classification_report (result2, testY))
