# code has been inferred from https://github.com/aGIToz/kFineTuning/blob/master/finetune.py
# https://keras.io/preprocessing/image/


import os
import seaborn as sns
import itertools
import numpy as np
import sys
import pandas as pd
import xml.etree.ElementTree as ET
from PIL import Image
from collections import Counter
from keras.models import Model
from keras import backend as K
from keras.callbacks import Callback
from keras.layers import Dense
from pathlib import Path
from keras.applications.resnet50 import ResNet50
import matplotlib.pyplot as plt
from sklearn.metrics import (f1_score,
                             precision_score,
                             recall_score)

%matplotlib inline

from google.colab import drive
drive.mount('/content/gdrive')

def get_labels(annotations_dir, unique_labels=True):
    for annotation_file in annotations_dir.iterdir():
        with open(annotation_file) as f:
            yield xml_to_labels(f.read(), unique_labels)


# import cv2
path = '/content/gdrive/My Drive/Colab Notebooks/project_phase2/Pascal_VOC/JPEGImages/2008_007057.jpg'

plt.imshow(plt.imread(Path(path).expanduser()))
plt.axis('off');

path1 = '/content/gdrive/My Drive/Colab Notebooks/project_phase2/Pascal_VOC/Annotations'
annotations_dir = Path(path1).expanduser()
images_dir = Path('/content/gdrive/My Drive/Colab Notebooks/project_phase2/Pascal_VOC/JPEGImages').expanduser()

img_metadata = pd.DataFrame(get_labels(annotations_dir), columns=['filename', 'labels'])
img_metadata.sample(7)


image_directory = Path('VOC2012/JPEGImages')
observation = img_metadata.sample(n=1).to_dict(orient='records')[0]
img = plt.imread(images_dir.joinpath(observation['filename']))      
img_gen = ImageDataGenerator(rescale=1/255, validation_split=0.2)


img_iter = img_gen.flow_from_dataframe(
    img_metadata,
    shuffle=True,
    directory=images_dir,
    x_col='filename',
    y_col='labels',
    class_mode='categorical',
    target_size=(128, 128),
    batch_size=20,
    subset='training'
)

img_iter_val = img_gen.flow_from_dataframe(
    img_metadata,
    shuffle=False,
    directory=images_dir,
    x_col='filename',
    y_col='labels',
    class_mode='categorical',
    target_size=(128, 128),
    batch_size=20,
    subset='validation'
)


label_to_class = {v: k for k, v in img_iter.class_indices.items()}
def array_to_labels(onehot_array, label_to_class):
    labels = []
    idx = np.where(onehot_array == 1)[0]
    return [label_to_class[i] for i in idx]
  
 
  
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array, load_img

from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.densenet import DenseNet121

E_model_Res = ResNet50(weights = 'imagenet', include_top = False, input_shape=(128, 128, 3))


print('Number of trainable weights before freezing the conv base:', len(E_model_Res.trainable_weights))
E_model_Res.trainable = False
print('Number of trainable weights after freezing the conv base:', len(E_model_Res.trainable_weights))


E_model1 = models.Sequential()
E_model1.add(E_model_Res)
E_model1.add(layers.Flatten())
E_model1.add(layers.Dense(256, activation='relu'))
E_model1.add(layers.Dense(20, activation='sigmoid'))

E_model1.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])

metrics = Metrics(img_iter_val, validation_steps=10)
history = E_model1.fit_generator(
    img_iter,
    epochs=1,
    steps_per_epoch=1,
    class_weight=class_weights,
    callbacks=[metrics]
)


total_counts = sum(labels_count.values())
class_weights = {img_iter.class_indices[cls]: total_counts / count for cls, count in labels_count.items()}

nr_batches = 10
threshold = 0.5
img_iter_val_0, img_iter_val_1 = itertools.tee(img_iter_val, 2)
y_true = np.vstack(next(img_iter_val_0)[1] for _ in range(nr_batches)).astype('int')
y_pred = (model.predict_generator(img_iter_val_1, steps=nr_batches) > threshold).astype('int')
y_pred = (E_model1.predict_generator(img_iter_val_1, steps=nr_batches) > threshold).astype('int')
print(y_pred)
