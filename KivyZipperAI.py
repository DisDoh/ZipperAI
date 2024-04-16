#Copyright 2024 Reda Benjamin Meyer

import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
import numpy as np
import os
import matplotlib.pyplot as plt

import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from zipfile import ZipFile


# Function to chunk and pad the bit sequence
def chunk_data(bit_sequence, chunk_size):
    """Chunk and pad the bit sequence to ensure each chunk is of size 1024."""
    num_chunks = len(bit_sequence) // chunk_size
    remainder = len(bit_sequence) % chunk_size
    chunks = [bit_sequence[i * chunk_size: (i + 1) * chunk_size] for i in range(num_chunks)]
    if remainder > 0:
        # Append the last chunk that contains the remainder of the data
        remainder_chunk = bit_sequence[-remainder:]
        # Create a padded version of the last chunk
        padded_chunk = np.pad(remainder_chunk, (0, chunk_size - remainder), mode='constant',
                              constant_values=0)
        chunks.append(padded_chunk)
    return chunks


# Function to remove padding from reconstructed data
def remove_padding(reconstructed_data, original_lengths):
    reconstructed_data_trimmed = []
    start_index = 0
    for length in original_lengths:
        reconstructed_data_trimmed.append(reconstructed_data[start_index:start_index + length])
        start_index += length
    return np.concatenate(reconstructed_data_trimmed)

def autoencoder(input_shape, encoding_dim):
    # --- Encoding Part ---
    input_data = layers.Input(shape=input_shape)
    encoded = layers.Dense(256, activation='relu')(input_data)
    encoded = layers.BatchNormalization()(encoded)
    encoded = layers.Dense(128, activation='relu')(encoded)
    encoded = layers.BatchNormalization()(encoded)
    encoded = layers.Dense(64, activation='relu')(encoded)
    encoded = layers.BatchNormalization()(encoded)
    encoded = layers.Dense(encoding_dim, activation='relu')(encoded)

    # --- Decoding part ---
    decoded = layers.Dense(64, activation='relu')(encoded)
    decoded = layers.BatchNormalization()(decoded)
    decoded = layers.Dense(128, activation='relu')(decoded)
    decoded = layers.BatchNormalization()(decoded)
    decoded = layers.Dense(256, activation='relu')(decoded)
    decoded = layers.BatchNormalization()(decoded)
    decoded = layers.Dense(input_shape[0], activation='sigmoid')(decoded)

    # Defining the models
    autoencoder_model = models.Model(input_data, decoded)  # Complete autoencoder = encoder + decoder
    encoder = models.Model(input_data, encoded)  # Just the encoder part

    # Now the decoder part
    encoded_input = layers.Input(shape=(encoding_dim,))
    decoder_layers = autoencoder_model.layers[-7:]  # Last 5 layers = decoder
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
        if epoch % 50 == 0:
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


class ZipApp(App):
    def build(self):
        self.title = 'File Zipper'

        # Layout
        layout = BoxLayout(orientation='vertical', padding=10)

        # File chooser
        self.file_chooser = FileChooserListView(path=os.path.expanduser('~') + '/Documents')
        self.file_chooser.filters = [lambda folder, filename: os.path.isfile(os.path.join(folder, filename))]
        layout.add_widget(self.file_chooser)

        # Label to display selected file path
        self.selected_file_label = Label(text="Selected file: None")
        layout.add_widget(self.selected_file_label)

        # Button to zip the file
        zip_button = Button(text='Zip Selected File', size_hint=(1, 0.1))
        zip_button.bind(on_press=self.zip_selected_file)
        layout.add_widget(zip_button)

        # Button to unzip the file
        unzip_button = Button(text='Unzip Selected File', size_hint=(1, 0.1))
        unzip_button.bind(on_press=self.unzip_selected_file)
        layout.add_widget(unzip_button)

        # Button to zip the file
        AI_zip_button = Button(text='AI Zip Selected File', size_hint=(1, 0.1))
        AI_zip_button.bind(on_press=self.AI_zip_selected_file)
        layout.add_widget(AI_zip_button)

        # Button to unzip the file
        AI_unzip_button = Button(text='AI Unzip Selected File', size_hint=(1, 0.1))
        AI_unzip_button.bind(on_press=self.AI_unzip_selected_file)
        layout.add_widget(AI_unzip_button)
        import random

        def generate_difficult_to_compress_file(file_path, size):
            with open(file_path, 'wb') as file:
                for _ in range(size):
                    # Generate a random byte value (0-255)
                    byte = random.randint(0, 255)
                    # Write the byte to the file
                    file.write(byte.to_bytes(1, byteorder='big'))

        # Example usage
        file_path = "difficult_to_compress.bin"
        file_size = 72  # Size in bytes

        generate_difficult_to_compress_file(file_path, file_size)
        print(f"Difficult-to-compress file '{file_path}' created with size {file_size} bytes.")

        return layout

    def zip_selected_file(self, instance):
        selected_file = self.file_chooser.selection[0] if self.file_chooser.selection else None

        if selected_file:
            zip_file_name = os.path.splitext(selected_file)[0] + '.zip'
            with ZipFile(zip_file_name, 'w') as zipf:
                zipf.write(selected_file, os.path.basename(selected_file))
            self.selected_file_label.text = f"File zipped and saved as: {zip_file_name}"
        else:
            self.selected_file_label.text = "Please select a file to zip"

    def unzip_selected_file(self, instance):
        selected_file = self.file_chooser.selection[0] if self.file_chooser.selection else None

        if selected_file and selected_file.endswith('.zip'):
            with ZipFile(selected_file, 'r') as zipf:
                zipf.extractall(os.path.dirname(selected_file))
            self.selected_file_label.text = "File unzipped successfully"
        else:
            self.selected_file_label.text = "Please select a zip file to unzip"
    def AI_zip_selected_file(self, instance):
        import numpy as np
        import h5py  # If loading HDF5 files

        selected_file = self.file_chooser.selection[0] if self.file_chooser.selection else None

        if selected_file:

            # Reshape the data as needed
            # For example, if you know the shape beforehand:
            # data = data.reshape((-1, 10))  # Assuming input data size of 10

            # Or if you need to determine the shape dynamically:
            # input_shape = (10,)  # Assuming input data size of 10
            # num_samples = len(data) // np.prod(input_shape)
            # data = data[:num_samples * np.prod(input_shape)].reshape((num_samples, *input_shape))

            # Define your input_shape and encoding_dim
            input_shape = (8,)  # Assuming input data size of 8
            encoding_dim = 3  # Adjust the encoding dimension as needed

            # Generate synthetic data
            num_samples = 5096
            data = np.random.randint(2, size=(num_samples, *input_shape))  # Generate random 0s and 1s

            autoencoder_model, encoder, decoder = autoencoder(input_shape, encoding_dim)

            threshold_callback = ThresholdCallback(threshold=0.0001)
            autoencoder_model.compile(optimizer='adam', loss='binary_crossentropy')

            # Loading saved models
            if os.path.exists('encoder_model_zip-BatchNorm-8-3.keras') and os.path.exists('decoder_weights_binary.weights-BatchNorm-8-3.h5'):
                encoder = models.load_model('encoder_model_zip-BatchNorm-8-3.keras')
                decoder.load_weights('decoder_weights_binary.weights-BatchNorm-8-3.h5')

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
             # Save the encoder model
            #encoder.save('encoder_model_zip-BatchNorm-8-3.keras')

            # # Save the decoder weights
            # decoder.save_weights('decoder_weights_binary.weights.h5')
            #
            # # Encode and decode the data
            # encoded_data = encoder.predict(data)
            #
            # decoded_data = decoder.predict(encoded_data)
            #
            # # Check if original data and reconstructed data are the same
            # if np.array_equal(data, np.round(decoded_data)):
            #     print("Original data and Reconstructed data are the same.")
            # else:
            #     print("Original data and Reconstructed data are different.")

            with open(selected_file, 'rb') as f:
                # Read binary data
                binary_data = f.read()

            def binary_to_bit_array(binary_data):
                """Convert binary data to a bit array."""
                bit_array = np.unpackbits(np.frombuffer(binary_data, dtype=np.uint8))
                return bit_array

            # Convert the PDF binary data to a bit array
            bit_array = binary_to_bit_array(binary_data)
            # Chunk the bit sequence into 1024-bit chunks
            chunk_size = input_shape[0]
            data_chunks = chunk_data(bit_array, chunk_size)

            # Reconstruct the data chunk by chunk using the specific model for each chunk
            reconstructed_data = []
            compressed_data = []
            original_lengths = []  # Store original lengths of each chunk

            for i, chunk in enumerate(data_chunks):
                # Assuming data_chunks contains binary data (0s and 1s)
                chunk = np.array(list(chunk), dtype=np.uint8)  # Convert binary data to uint8 array
                chunk = np.expand_dims(chunk, axis=0)

                compressed_chunk = encoder.predict(chunk)
                compressed_data.append(np.round(compressed_chunk))
                reconstructed_chunk = decoder.predict(compressed_chunk)
                print(f"{i}/{len(data_chunks)}")

                # Remove padding from the reconstructed chunk
                reconstructed_chunk = remove_padding(reconstructed_chunk.squeeze(), [len(chunk[0])])

                reconstructed_data.append(reconstructed_chunk)  # Remove batch dimension

                # Store original length of chunk
                original_lengths.append(len(chunk[0]))
            # Assume compressed_data is ready and scaled appropriately
            # Convert to uint8 if not already done. This is necessary for byte conversion.
            compressed_data = np.array(compressed_data)
            compressed_data_uint8 = compressed_data.astype(np.uint8)

            # Convert to bytes
            compressed_data_bytes = compressed_data_uint8.tobytes()

            # Write to binary file
            with open(f'{selected_file}.AIZip', 'wb') as file:
                file.write(compressed_data_bytes)

            self.selected_file_label.text = f"File zipped and saved as: {selected_file}.AIZip"
        else:
            self.selected_file_label.text = "Please select a file to zip"


    def AI_unzip_selected_file(self, instance):
        selected_file = self.file_chooser.selection[0] if self.file_chooser.selection else None

        if selected_file and selected_file.endswith('.AIZip'):
            # Load the compressed binary AI file
            with open(selected_file, 'rb') as file:
                compressed_data_bytes = file.read()

            # Convert compressed data bytes back to numpy array of uint8
            compressed_data_uint8 = np.frombuffer(compressed_data_bytes, dtype=np.uint8)

            input_shape = (8,)
            encoding_dim = 3
            # Reshape the compressed data to the shape of (num_chunks, 4)
            num_chunks = len(compressed_data_uint8) // encoding_dim
            compressed_data = compressed_data_uint8[:num_chunks * encoding_dim].reshape((num_chunks, encoding_dim))
            autoencoder_model, encoder, decoder = autoencoder(input_shape, encoding_dim)

            # Load the decoder model
            decoder.load_weights('decoder_weights_binary.weights-BatchNorm-8-3.h5')
            # Decode the compressed data to obtain the original data
            original_data = []
            reconstructed_data = []

            for i, chunk in enumerate(compressed_data):
                # Assuming each chunk is of size (4,)
                chunk = np.expand_dims(chunk, axis=0)  # Add batch dimension
                # decoded_chunk = decoder.predict(chunk)
                reconstructed_chunk = decoder.predict(chunk)
                print(f"{i}/{len(compressed_data)}")

                # Remove padding from the reconstructed chunk
                reconstructed_chunk = remove_padding(reconstructed_chunk.squeeze(), [input_shape[0]])

                reconstructed_data.append(reconstructed_chunk)  # Remove batch dimension

                # Store original length of chunk
                #original_lengths.append(len(chunk[0]))

            # Convert the reconstructed data from uint8 back to binary (0s and 1s) before saving
            reconstructed_data = np.round(reconstructed_data, 0)  # Convert probabilities to binary
            reconstructed_data = reconstructed_data.astype(np.uint8)

            # Convert the numpy arrays in reconstructed_data to binary strings
            reconstructed_data = [''.join(map(str, map(int, b))) for b in reconstructed_data]

            def chunk_string(string, size):
                return [string[i:i + size] for i in range(0, len(string), size)]

            reconstructed_data_bit_chunks = [chunk_string(b, 8) for b in reconstructed_data]

            byte_array = bytearray([int(b, 2) for sublist in reconstructed_data_bit_chunks for b in sublist])

            # Write the original data to a file or use it as needed
            with open(selected_file[:-6], 'wb') as file:  # Remove the '.AIZip' extension
                file.write(byte_array)

            self.selected_file_label.text = f"File unzipped and saved as: {selected_file[:-6]}"
        else:
            self.selected_file_label.text = "Please select a valid .AIZip file"




if __name__ == '__main__':
    ZipApp().run()
