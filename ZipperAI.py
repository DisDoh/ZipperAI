import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
import os
import pickle

# Define the autoencoder architecture with additional hidden layers
def autoencoder(input_shape, encoding_dim):
    # Encoder
    # Encoder
    input_data = layers.Input(shape=input_shape)
    encoded = layers.Dense(encoding_dim, activation='relu')(input_data)

    # Decoder
    decoded = layers.Dense(input_shape[0], activation='relu')(encoded)

    # Autoencoder model
    autoencoder_model = models.Model(input_data, decoded)

    # Encoder model
    encoder_model = models.Model(input_data, encoded)

    # Decoder model
    decoder_input = layers.Input(shape=(encoding_dim,))
    decoder_output = autoencoder_model.layers[-1](decoder_input)
    decoder_model = models.Model(decoder_input, decoder_output)

    return autoencoder_model, encoder_model, decoder_model

# Generate some dummy data
data = np.round(np.random.rand(1, 1024), 0)  # Assuming MNIST-like data with 784 features

# Normalize the data
data /= np.max(data)

# Split data into training and validation sets
train_size = int(1 * len(data))
train_data, val_data = data, data[train_size:]

# Define autoencoder parameters
input_shape = (1024,)  # Assuming MNIST-like data
encoding_dim = int(1024 / 2)  # Size of the compressed representation

# Check if a model exists, if yes, load it
if os.path.exists('autoencoder_model_zip.keras'):
    autoencoder_model = tf.keras.models.load_model('autoencoder_model_zip.keras')
    encoder_model = tf.keras.models.load_model('encoder_model_zip.keras')
    decoder_model = tf.keras.models.load_model('decoder_model_zip.keras')
    print("Loaded existing model.")
else:
    # Create the autoencoder if no model exists
    autoencoder_model, encoder_model, decoder_model = autoencoder(input_shape, encoding_dim)

# Define custom callback to stop training if loss falls below a threshold
class ThresholdCallback(callbacks.Callback):
    def __init__(self, threshold):
        super(ThresholdCallback, self).__init__()
        self.threshold = threshold

    def on_epoch_end(self, epoch, logs=None):
        if logs['loss'] <= self.threshold:
            print(f"\nReached loss threshold of {self.threshold}. Stopping training.")
            self.model.stop_training = True
autoencoder_model.compile(optimizer='adam', loss='binary_crossentropy')
threshold_callback = ThresholdCallback(threshold=1e-9)
# Train the autoencoder with validation data
history = autoencoder_model.fit(train_data, train_data, epochs=10000, batch_size=256, shuffle=True,
                                callbacks=[threshold_callback])

# Save models and training history
autoencoder_model.save('autoencoder_model_zip.keras')
encoder_model.save('encoder_model_zip.keras')
decoder_model.save('decoder_model_zip.keras')

# Save the training history as a pickle file
with open('training_history.pkl', 'wb') as file:
    pickle.dump(history.history, file)

# Test the autoencoder
encoded_data = encoder_model.predict(data)
decoded_data = decoder_model.predict(encoded_data)

# Print reconstructed data and original data
print("Original data shape:", data.shape)
print("Reconstructed data shape:", decoded_data.shape)

# Print reconstructed data and original data
print("Original data:", np.round(data,0))
print("Reconstructed data:", np.round(decoded_data,0))

# Compare hashes
import hashlib
md5_hash_original = hashlib.md5(data).hexdigest()
md5_hash_reconstructed = hashlib.md5(decoded_data).hexdigest()
if md5_hash_original == md5_hash_reconstructed:
    print("True")
else:
    print("False")
