import tensorflow as tf
import time
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
plt.style.use("fivethirtyeight")

def create_model(LOSS_FUNCTION, OPTIMIZER, METRICS, NUM_CLASSES):
    LAYERS = [
          tf.keras.layers.Flatten(input_shape=[28,28], name="inputLayer"),
          tf.keras.layers.Dense(300, activation="relu", name="hiddenLayer1"),
          tf.keras.layers.Dense(100, activation="relu", name="hiddenLayer2"),
          tf.keras.layers.Dense(10, activation="softmax", name="outputLayer")]
    model_clf = tf.keras.models.Sequential(LAYERS)
    
    model_clf.summary()

    LOSS_FUNCTION = "sparse_categorical_crossentropy"
    OPTIMIZER = "SGD"
    METRICS = ["accuracy"]

    model_clf.compile(loss=LOSS_FUNCTION, optimizer=OPTIMIZER, metrics=METRICS)
    return model_clf  # << untrained Model


def get_unique_filename(filename):
    unique_filename = time.strftime(f"%Y%m%d_%H%M%S{filename}")
    return unique_filename


def save_model(model, model_name, model_dir):
    unique_filename = get_unique_filename(model_name)
    path_to_model = os.path.join(model_dir, unique_filename)
    print(path_to_model)
    model.save(path_to_model)


def save_plot(df, file_name, model, plot_dir):
    df.plot(figsize=(10, 7))
    plt.grid(True)
    unique_filename = get_unique_filename(file_name)
    path_to_model = os.path.join(plot_dir, unique_filename)
    plt.savefig(path_to_model)


def prepare_data(df):
  X = df.drop("y", axis=1)

  y = df["y"]

  return X, y