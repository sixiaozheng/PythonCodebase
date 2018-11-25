## convert csv files to tfrecord
import tensorflow as tf
import numpy as np
import pandas as pd

train_frame = pd.read_csv("./data/train.csv")
print(train_frame.head())
train_labels_frame = train_frame.pop(item="label")
train_values = train_frame.values
train_labels = train_labels_frame.values
print("values shape: ", train_values.shape)
print("labels shape:", train_labels.shape)

writer = tf.python_io.TFRecordWriter("csv_train.tfrecords")

for i in range(train_values.shape[0]):
    image_raw = train_values[i].tostring()
    example = tf.train.Example(
        features=tf.train.Features(
            feature={
                "image_raw": tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_raw])),
                "label": tf.train.Feature(int64_list=tf.train.Int64List(value=[train_labels[i]]))
            }
        )
    )
    writer.write(record=example.SerializeToString())

writer.close()