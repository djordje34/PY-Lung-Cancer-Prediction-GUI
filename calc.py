import os
import tempfile

import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from matplotlib import pyplot as plt


def getAnalysis(vals):
    vals = tf.convert_to_tensor(np.array(vals),dtype=tf.int64)
    try:
        model = tf.keras.models.load_model('checkpoints/model')
    except:
        return "Model not loaded. Please run setup.py."
    prediction = model.predict(vals)
    
    return prediction





def structureAnalysis(data):
    df = pd.read_csv("data.csv")
    max_bound,min_bound = df["factor"].max(),df["factor"].min()
    
    #minimum val append to max and to res, and then calculate
    if(getAnalysis(data)== "Model not loaded. Please run setup.py."):
        return getAnalysis(data)
    
    res = getAnalysis(data)[0][0]
    max_bound = max_bound + abs(min_bound)
    res +=abs(min_bound)
    
    return (f"There's a {round(abs(res/max_bound)*100,0)}% chance that you could have developed lung cancer,\n which means that among tested people with similar symptoms, {round(abs(res/max_bound)*100,0)}% have got lung cancer.\nThis is an analysis based on ~300 people tested.\n If you do have any of the expressed symptoms,\n you should consult with a professional no matter what results this application gives you.\nUnpredictable input will result in an anomaly,\nfor example: birth year being 1990,2023 etc...")
    


