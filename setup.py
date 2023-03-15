"""
    https://www.kaggle.com/datasets/mysarahmadbhat/lung-cancer
    
    Total no. of attributes:16
No .of instances:284
Attribute information:

Gender: M(male), F(female)
Age: Age of the patient
Smoking: YES=2 , NO=1.
Yellow fingers: YES=2 , NO=1.
Anxiety: YES=2 , NO=1.
Peer_pressure: YES=2 , NO=1.
Chronic Disease: YES=2 , NO=1.
Fatigue: YES=2 , NO=1.
Allergy: YES=2 , NO=1.
Wheezing: YES=2 , NO=1.
Alcohol: YES=2 , NO=1.
Coughing: YES=2 , NO=1.
Shortness of Breath: YES=2 , NO=1.
Swallowing Difficulty: YES=2 , NO=1.
Chest pain: YES=2 , NO=1.
Lung Cancer: YES , NO.
    
    
"""

import os
import tempfile

import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from matplotlib import pyplot as plt

SHUFFLE_BUFFER = 500
BATCH_SIZE = 2


def get_basic_model(normalizer):
    model = tf.keras.Sequential([
    normalizer,
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(1)
  ])

    model.compile(optimizer='adam',
                loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                metrics=['accuracy'])
    return model
def rnd(x):
    
    return int(x>0)

def main():
    df = pd.read_csv("survey lung cancer.csv")
    #ne treba shuffle->data vec izmesana
    df = df.iloc[:len(df.index)//4*3]
    toPredict = df.iloc[len(df.index)//4*3:]
    
    target = df.pop("LUNG_CANCER")


    toPredict.loc[toPredict["LUNG_CANCER"]=="YES","LUNG_CANCER"] = 1
    toPredict.loc[toPredict["LUNG_CANCER"]=="NO","LUNG_CANCER"] = 0    
    target[target=="YES"] = 1
    target[target=="NO"] = 0
    df.loc[df["GENDER"]=="M","GENDER"],df.loc[df["GENDER"]=="F","GENDER"] = 0,1

    
    df = tf.convert_to_tensor(np.array(df),dtype=tf.int64)
    target = tf.convert_to_tensor(np.array(target),dtype=tf.int64)
    
    temp = toPredict.drop(["LUNG_CANCER"],axis = 1)
    
    temp = tf.convert_to_tensor(np.array(temp),dtype=tf.int64)
    
    
    normalizer = tf.keras.layers.Normalization(axis=-1)
    normalizer.adapt(df)

    model = get_basic_model(normalizer)

    
    model.fit(df, target, epochs=50, batch_size=BATCH_SIZE)
    
    
    prediction = model.predict(temp)
    toPredict["factor"] = prediction
    rounder = np.vectorize(rnd)
    prediction = rounder(prediction)
    toPredict['predicted'] = prediction

    toPredict['pctg'] = toPredict['LUNG_CANCER']-toPredict['predicted']
    
    accuracy = (toPredict['pctg'].count()-toPredict.loc[toPredict['pctg']!=0,"pctg"].count())/toPredict['pctg'].count()
    print(accuracy)
    model.save('checkpoints/model')
    toPredict.to_csv("data.csv",index=None)

    
    
if __name__=="__main__":
    main()