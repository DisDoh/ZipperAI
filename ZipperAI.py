import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
import numpy as np
import os
import matplotlib.pyplot as plt

def autoencoder(input_shape, encoding_dim):
    # --- Encoding Part ---
    input_data = layers.Input(shape=input_shape)
    encoded = layers.Dense(512, activation='sigmoid')(input_data)
    encoded = layers.Dropout(0.5)(encoded)
    encoded = layers.Dense(256, activation='sigmoid')(encoded)
    encoded = layers.Dense(encoding_dim, activation='sigmoid')(encoded)

    # --- Decoding part ---
    decoded = layers.Dense(256, activation='sigmoid')(encoded)
    decoded = layers.Dense(512, activation='sigmoid')(decoded)
    decoded = layers.Dense(input_shape[0], activation='sigmoid')(decoded)

    # Defining the models
    autoencoder_model = models.Model(input_data, decoded)  # Complete autoencoder = encoder + decoder
    encoder = models.Model(input_data, encoded)  # Just the encoder part

    # Now the decoder part
    encoded_input = layers.Input(shape=(encoding_dim,))
    decoder_layers = autoencoder_model.layers[-3:]  # Last 3 layers = decoder
    decoder = encoded_input
    for layer in decoder_layers:
        decoder = layer(decoder)
    decoder = models.Model(encoded_input, decoder)

    return autoencoder_model, encoder, decoder



# Define custom callback to stop training if loss falls below a threshold
class ThresholdCallback(callbacks.Callback):
    def __init__(self, threshold):
        super(ThresholdCallback, self).__init__()
        self.threshold = threshold

        self.val_loss = []
        self.loss = []
    def on_epoch_end(self, epoch, logs=None):
        self.loss.append(logs['loss'])
        self.val_loss.append(logs['val_loss'])
        if epoch % 10 == 0:
            # Plot the loss
            plt.plot(self.loss, label='Training Loss')
            plt.plot(self.val_loss, label='Validation Loss')
            plt.xlabel('Epochs')
            plt.ylabel('Loss')
            plt.title('Loss vs. Epochs')
            plt.legend()
            plt.grid(True)
            plt.show()
        if epoch % 200 == 0:
            self.loss = []
            self.val_loss = []
        if logs['loss'] <= self.threshold:
            print(f"\nReached loss threshold of {self.threshold}. Stopping training.")
            self.model.stop_training = True


# Define your input_shape and encoding_dim
input_shape = (8,)  # Assuming input data size of 1024
encoding_dim = 4  # Adjust the encoding dimension as needed

# Generate synthetic data
num_samples = 4096
data = np.random.binomial(1, 0.5, size=(num_samples, *input_shape))

# Split data into training and validation sets
validation_split = 0.3
num_validation_samples = int(num_samples * validation_split)
x_train = data[num_validation_samples:]
x_val = data[:num_validation_samples]

autoencoder_model, encoder, decoder = autoencoder(input_shape, encoding_dim)

threshold_callback = ThresholdCallback(threshold=0.001)
autoencoder_model.compile(optimizer='adam', loss='binary_crossentropy')

with open('data.bin', 'wb') as f:
    f.write(data.tobytes())
f.close()
# Loading saved models
if os.path.exists('encoder_model_zip.keras') and os.path.exists('decoder_model_zip.keras'):
    encoder = models.load_model('encoder_model_zip.keras')
    decoder = models.load_model('decoder_model_zip.keras')

    # Load your test data here
    # For demonstration, let's assume you have test_data

    # Test the encoder and decoder with the test data
    test_encoded_data = encoder.predict(data)
    test_decoded_data = decoder.predict(test_encoded_data)

    # Check if original data and reconstructed data are the same
    if np.array_equal(data, np.round(test_decoded_data)):
        print("Original data and Reconstructed data are the same.")
    else:
        print("Original data and Reconstructed data are different.")
else:
    print("No saved models found.")
# Train the model with validation data
    history = autoencoder_model.fit(x_train, x_train, epochs=100000, shuffle=True, batch_size=64,
                                validation_data=(x_val, x_val),
                                callbacks=[threshold_callback])

encoder.save('encoder_model_zip.keras')
autoencoder_model.save('autoencoder_model_zip.keras')
decoder.save('decoder_model_zip.keras')

# FIX: compute encoded and decoded data
encoded_data = encoder.predict(data)
decoded_data = decoder.predict(encoded_data)  # Reconstructed data

# Check if original data and reconstructed data are the same
if np.array_equal(data, np.round(decoded_data)):
    print("Original data and Reconstructed data are the same.")
else:
    print("Original data and Reconstructed data are different.")
