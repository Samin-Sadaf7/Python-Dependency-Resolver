import tensorflow as tf
from tensorflow.keras import layers

model = tf.keras.Sequential([
    layers.Dense(10, input_shape=(5,))
])
model.compile(optimizer='adam', loss='mse')
print("Model created successfully!")