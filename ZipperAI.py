import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
import os
import hashlib
import numpy as np
import pickle

def autoencoder(input_shape, encoding_dim):
    input_data = layers.Input(shape=input_shape)
    encoded = layers.Dense(encoding_dim, activation='relu')(input_data)

    # At this point the representation is (encoding_dim)-dimensional
    decoded = layers.Dense(input_shape[0], activation='sigmoid')(encoded)

    # This model maps an input to its reconstruction
    autoencoder_model = models.Model(input_data, decoded)

    # This model maps an input to its encoded representation
    encoder = models.Model(input_data, encoded)

    # Create a placeholder for an encoded input
    encoded_input = layers.Input(shape=(encoding_dim,))

    # Retrieve the last layer of the autoencoder model
    decoder_layer = autoencoder_model.layers[-1]

    # Create the decoder model
    decoder = models.Model(encoded_input, decoder_layer(encoded_input))

    return autoencoder_model, encoder, decoder


# Define custom callback to stop training if loss falls below a threshold
class ThresholdCallback(callbacks.Callback):
    def __init__(self, threshold):
        super(ThresholdCallback, self).__init__()
        self.threshold = threshold

    def on_epoch_end(self, epoch, logs=None):
        if logs['loss'] <= self.threshold:
            print(f"\nReached loss threshold of {self.threshold}. Stopping training.")
            self.model.stop_training = True


# Define your input_shape and encoding_dim
input_shape = (1024,)  # Replace YOUR_DIM with the actual dimension
encoding_dim = 1  # Replace YOUR_ENCODING_DIM with the actual dimension

# Define the data here
data_size = 1  # Replace this with the size of your data
data = np.random.binomial(1, 0.5, size=(data_size, *input_shape))
autoencoder_model, encoder, decoder = autoencoder(input_shape, encoding_dim)

if os.path.exists('encoder_model_zip.keras'):
    #autoencoder_model = tf.keras.models.load_model('autoencoder_model_zip.keras')

    encoder = tf.keras.models.load_model('encoder_model_zip.keras')
    decoder = tf.keras.models.load_model('decoder_model_zip.keras')

    shape = data.shape
    dtype = data.dtype

    with open("data.bin", "rb") as f:
        loaded_data = np.frombuffer(f.read(), dtype=dtype)
        data = loaded_data.reshape(shape)  # Original shape
    # Reach the end of file
    f.close()
    print("Loaded existing model.")
else:
    threshold_callback = ThresholdCallback(threshold=0.01)
    autoencoder_model.compile(optimizer='adam', loss='binary_crossentropy')


    # Saving data with pickle
    with open('data.bin', 'wb') as f:
        f.write(data.tobytes())
    # Reach the end of file
    f.close()
    # Adjust the number of epochs and the batch size as needed
    autoencoder_model.fit(data, data, epochs=100, batch_size=32, shuffle=True, callbacks=[threshold_callback])

    #autoencoder_model.save('autoencoder_model_zip.keras')
    encoder.save('encoder_model_zip.keras')
    decoder.save('decoder_model_zip.keras')


# FIX: compute encoded and decoded data
encoded_data = encoder.predict(data)
decoded_data = decoder.predict(encoded_data)  # Reconstructed data

# Generate compressed data and reconstruct
compressed_data = encoder.predict(data)
reconstructed_data = decoder.predict(compressed_data)

# Convert reconstructed data to binary format
reconstructed_data_binary = np.where(reconstructed_data > 0.5, 1, 0)

# Check if original data and reconstructed data are the same
if np.array_equal(data, reconstructed_data_binary):
    print("Original data and Reconstructed data are the same.")
else:
    print("Original data and Reconstructed data are different.")