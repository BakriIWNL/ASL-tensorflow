import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import gc
from keras.models import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dense, Flatten
import cv2
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import classification_report, confusion_matrix
import skimage
from skimage.transform import resize
import tensorflow as tf
from tensorflow import keras
import os

model = load_model('ASL2.h5')

label_mapping = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
        'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'del': 26,
        'nothing': 27, 'space': 28}

while True:
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            frame = cv2.flip(frame, 1)
            img = frame
            imgcopy = img.copy()
            break

    cap.release()
    cv2.destroyAllWindows()

    img_file = skimage.transform.resize(img, (32, 32, 3))
    img_arr = np.asarray(img_file).reshape((-1, 32, 32, 3))

    cv2.putText(imgcopy, 'Predicting!', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('Predicting', imgcopy)

    predictions = model.predict(img_arr, verbose=0)
    print(predictions)
    predictions = np.argmax(predictions, axis=1)
    for i, x in label_mapping.items():
        if x == predictions[0]:
            predictions = i
    print(predictions)
    cv2.destroyAllWindows()
    
    while True:
        cv2.putText(img, str(predictions[0]), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow('Image', img)
        if cv2.waitKey(1) & 0xFF == ord('n'):
            flag = 0
            break
        if cv2.waitKey(1) & 0xFF == ord('y'):
            flag = 1
            break
    cv2.destroyAllWindows()
    if flag == 1:
        continue
    else:
        break
