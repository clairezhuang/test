# Databricks notebook source
# MAGIC %fs ls

# COMMAND ----------

from tensorflow.keras.models import Model, save_model
import tensorflow as tf
import datetime
import random
import shutil
now = datetime.datetime.now()
task_id = now.strftime("%y%m%d%H%M%S") + str(random.randint(100, 999))
path= "/Volumes/ml/default/volume1/"
tmp_path = rf"{task_id}.h5"
model2 = tf.keras.models.load_model("/Volumes/ml/default/volume1/mnist-model.h5")
save_model(model2, tmp_path)
print("test1")
