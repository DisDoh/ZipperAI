#Copyright Reda Benjamin Meyer 2024

import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
import numpy as np
import os
import matplotlib.pyplot as plt

class RoundLayer(layers.Layer):
    def build(self, input_shape):
        # Create a trainable weight variable for the kernel
        self.kernel = self.add_weight(name='kernel', shape=(input_shape[-1],),
                                      initializer='ones', trainable=True)

        super().build(input_shape)

    def call(self, x):
        # Round the input tensor
        rounded_x = tf.round(x)

        # Round the kernel weights
        self.kernel.assign(tf.round(self.kernel))

        return rounded_x

    def compute_output_shape(self, input_shape):
        return input_shape

    def get_config(self):
        return super().get_config()
def autoencoder(input_shape, encoding_dim):
    # --- Encoding Part ---
    input_data = layers.Input(shape=input_shape)
    encoded = layers.Dense(128, activation='sigmoid')(input_data)
    encoded = layers.Dropout(0.3)(encoded)
    encoded = layers.Dense(64, activation='sigmoid')(encoded)
    encoded = layers.Dense(encoding_dim, activation='sigmoid')(encoded)

    # --- Decoding part ---
    decoded = layers.Dense(64, activation='sigmoid')(encoded)
    decoded = layers.Dense(128, activation='sigmoid')(decoded)
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
        if epoch % 46 == 0:
            # Plot the loss
            plt.plot(self.loss, label='Training Loss')
            plt.plot(self.val_loss, label='Validation Loss')
            plt.xlabel('Epochs')
            plt.ylabel('Loss')
            plt.title('Loss vs. Epochs')
            plt.legend()
            plt.grid(True)
            plt.show()
        if epoch % 400 == 0:
            self.loss = []
            self.val_loss = []
        if logs['loss'] <= self.threshold:
            print(f"\nReached loss threshold of {self.threshold}. Stopping training.")
            self.model.stop_training = True

# Define your input_shape and encoding_dim
input_shape = (8,)  # Assuming input data size of 8
encoding_dim = 1  # Adjust the encoding dimension as needed

# Generate synthetic data
num_samples = 40960
data = np.random.randint(2, size=(num_samples, *input_shape))  # Generate random 0s and 1s

# Split data into training and validation sets
validation_split = 0.3
num_validation_samples = int(num_samples * validation_split)
x_train = data[num_validation_samples:]
x_val = data[:num_validation_samples]

autoencoder_model, encoder, decoder = autoencoder(input_shape, encoding_dim)

threshold_callback = ThresholdCallback(threshold=0.01)
autoencoder_model.compile(optimizer='adam', loss='binary_crossentropy')

# Loading saved models
if os.path.exists('encoder_model_zip.keras') and os.path.exists('decoder_weights_binary.weights.h5'):
    encoder = models.load_model('encoder_model_zip.keras')
    decoder.load_weights('decoder_weights_binary.weights.h5')

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
# Save the encoder model
encoder.save('encoder_model_zip.keras')

# Save the decoder weights
decoder.save_weights('decoder_weights_binary.weights.h5')

# Encode and decode the data
encoded_data = encoder.predict(data)
decoded_data = decoder.predict(encoded_data)

# Check if original data and reconstructed data are the same
if np.array_equal(data, np.round(decoded_data)):
    print("Original data and Reconstructed data are the same.")
else:
    print("Original data and Reconstructed data are different.")

# Function to chunk and pad the bit sequence
def chunk_data(bit_sequence, chunk_size):
    num_chunks = len(bit_sequence) // chunk_size
    remainder = len(bit_sequence) % chunk_size
    chunks = [bit_sequence[i * chunk_size: (i + 1) * chunk_size] for i in range(num_chunks)]
    if remainder > 0:
        # Append the last chunk that contains the remainder of the data
        remainder_chunk = bit_sequence[-remainder:]
        chunks.append(remainder_chunk)
    return chunks

# Function to remove padding from reconstructed data
def remove_padding(reconstructed_data, original_lengths):
    reconstructed_data_trimmed = []
    start_index = 0
    for length in original_lengths:
        reconstructed_data_trimmed.append(reconstructed_data[start_index:start_index + length])
        start_index += length
    return np.concatenate(reconstructed_data_trimmed)

# Load your PDF file as binary data
filename = "test"
with open(filename, 'rb') as obj:
    pdf_binary_data = obj.read()

# Convert the PDF binary data to a bit sequence
bit_sequence = np.frombuffer(pdf_binary_data, dtype=np.uint8)
def binary_to_bit_array(binary_data):
    """Convert binary data to a bit array."""
    bit_array = np.unpackbits(np.frombuffer(binary_data, dtype=np.uint8))
    return bit_array

# Convert the PDF binary data to a bit array
bit_array = binary_to_bit_array(pdf_binary_data)
# Chunk the bit sequence into 1024-bit chunks
chunk_size = int(8)
data_chunks = chunk_data(bit_array, chunk_size)

# Define your input_shape and encoding_dim
input_shape = (8,)  # Assuming input data size of 1024
encoding_dim = 4  # Adjust the encoding dimension as needed

# Reconstruct the data chunk by chunk using the specific model for each chunk
reconstructed_data = []
compressed_data = []
original_lengths = []  # Store original lengths of each chunk

for i, chunk in enumerate(data_chunks):
    # Assuming data_chunks contains binary data (0s and 1s)
    chunk = np.array(list(chunk), dtype=np.float32)  # Convert binary data to float32 array
    chunk = np.expand_dims(chunk, axis=0)

    compressed_chunk = encoder.predict(chunk)
    compressed_data.append(compressed_chunk)
    reconstructed_chunk = decoder.predict(compressed_chunk)
    reconstructed_data.append(reconstructed_chunk.squeeze(0))  # Remove batch dimension
    print(f"{i}/{len(data_chunks)}")
    # Store original length of chunk
    original_lengths.append(len(chunk[0]))
# Assume compressed_data is ready and scaled appropriately
# Convert to uint8 if not already done. This is necessary for byte conversion.
compressed_data = np.array(compressed_data)
compressed_data_uint8 = compressed_data.astype(np.uint8)

# Convert to bytes
compressed_data_bytes = compressed_data_uint8.tobytes()

# Write to binary file
with open('compressed_data.bin', 'wb') as file:
    file.write(compressed_data_bytes)

# Convert the reconstructed data from float32 back to binary (0s and 1s) before saving
reconstructed_data = np.round(reconstructed_data, 0)  # Convert probabilities to binary
reconstructed_data = reconstructed_data.astype(np.uint8)

# Convert the numpy arrays in reconstructed_data to binary strings
reconstructed_data = [''.join(map(str, map(int, b))) for b in reconstructed_data]

byte_array = bytearray([int(b, 2) for b in reconstructed_data])

with open("reconstructed_binary_file", "wb") as f:
    f.write(byte_array)

print("Reconstructed binary file saved.")

reconstructed_data = []
for i, compressed_chunk in enumerate(compressed_data):

    reconstructed_chunk = decoder.predict(compressed_chunk)
    reconstructed_data.append(reconstructed_chunk.squeeze(0))  # Remove batch dimension
    print(f"{i}/{len(data_chunks)}")



# Convert the reconstructed data from float32 back to binary (0s and 1s) before saving
reconstructed_data = np.round(reconstructed_data, 0)  # Convert probabilities to binary
reconstructed_data = reconstructed_data.astype(np.uint8)

# Convert the numpy arrays in reconstructed_data to binary strings
reconstructed_data = [''.join(map(str, map(int, b))) for b in reconstructed_data]

byte_array = bytearray([int(b, 2) for b in reconstructed_data])

with open("reconstructed_binary_file_bis", "wb") as f:
    f.write(byte_array)