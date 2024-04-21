# Copyright 2024 Reda Benjamin Meyer

import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.models import load_model, model_from_json
import numpy as np
import os
import matplotlib.pyplot as plt



from keras import activations
from keras import backend
from keras import constraints
from keras import initializers
from keras import regularizers
from keras.dtensor import utils
from keras.engine.base_layer import Layer
from keras.engine.input_spec import InputSpec
import tensorflow as tf
from tensorflow.keras import activations, initializers, regularizers, constraints
from tensorflow.keras.layers import InputSpec
from tensorflow.keras.utils import register_keras_serializable

from tensorflow import cast

@register_keras_serializable(package='Custom', name='RoundLayer')
class RoundLayer(Layer):

    def __init__(
            self,
            units,
            activation=None,
            use_bias=True,
            kernel_initializer="glorot_uniform",
            bias_initializer="zeros",
            kernel_regularizer=None,
            bias_regularizer=None,
            activity_regularizer=None,
            kernel_constraint=None,
            bias_constraint=None,
            **kwargs,
    ):
        super().__init__(activity_regularizer=activity_regularizer, **kwargs)
        self.units = int(units) if not isinstance(units, int) else units
        if self.units < 0:
            raise ValueError(
                f"Received an invalid value for `units`, expected a positive integer. Received: units={units}")
        self.activation = activations.get(activation)
        self.use_bias = use_bias
        self.kernel_initializer = initializers.get(kernel_initializer)
        self.bias_initializer = initializers.get(bias_initializer)
        self.kernel_regularizer = regularizers.get(kernel_regularizer)
        self.bias_regularizer = regularizers.get(bias_regularizer)
        self.kernel_constraint = constraints.get(kernel_constraint)
        self.bias_constraint = constraints.get(bias_constraint)

        self.input_spec = InputSpec(min_ndim=2)
        self.supports_masking = True

    def build(self, input_shape):
        dtype = tf.as_dtype(self.dtype or tf.keras.backend.floatx())
        input_shape = tf.TensorShape(input_shape)
        last_dim = input_shape[-1]
        if last_dim is None:
            raise ValueError("The last dimension of the inputs to `RoundLayer` should be defined. Found `None`.")

        self.input_spec = InputSpec(min_ndim=2, axes={-1: last_dim})
        self.kernel = self.add_weight(
            "kernel",
            shape=[last_dim, self.units],
            initializer=self.kernel_initializer,
            regularizer=self.kernel_regularizer,
            constraint=self.kernel_constraint,
            dtype=self.dtype,
            trainable=True,
        )
        if self.use_bias:
            self.bias = self.add_weight(
                "bias",
                shape=[self.units],
                initializer=self.bias_initializer,
                regularizer=self.bias_regularizer,
                constraint=self.bias_constraint,
                dtype=self.dtype,
                trainable=True,
            )
        else:
            self.bias = None
        self.built = True

    def call(self, inputs):
        outputs = tf.matmul(inputs, self.kernel)
        if self.use_bias:
            outputs = tf.nn.bias_add(outputs, self.bias)
        # Apply rounding here to the outputs before activation
        rounded_outputs = tf.round(outputs)
        if self.activation is not None:
            return self.activation(rounded_outputs)
        return rounded_outputs

    def compute_output_shape(self, input_shape):
        input_shape = tf.TensorShape(input_shape)
        return input_shape[:-1].concatenate(self.units)

    def get_config(self):
        config = super().get_config()
        config.update({
            "units": self.units,
            "activation": activations.serialize(self.activation),
            "use_bias": self.use_bias,
            "kernel_initializer": initializers.serialize(self.kernel_initializer),
            "bias_initializer": initializers.serialize(self.bias_initializer),
            "kernel_regularizer": regularizers.serialize(self.kernel_regularizer),
            "bias_regularizer": regularizers.serialize(self.bias_regularizer),
            "activity_regularizer": regularizers.serialize(self.activity_regularizer),
            "kernel_constraint": constraints.serialize(self.kernel_constraint),
            "bias_constraint": constraints.serialize(self.bias_constraint),
        })
        return config


class RoundLayer_(layers.Layer):
    def __init__(self, activation='relu', **kwargs):
        super(RoundLayer, self).__init__(**kwargs)
        self.activation = tf.keras.activations.get(activation)

    def build(self, input_shape):
        # Adjusted kernel shape for proper matrix multiplication
        self.kernel = self.add_weight(name="kernel",
                                      shape=(input_shape[-1], input_shape[-1]),
                                      initializer='glorot_uniform',
                                      trainable=True)
        self.bias = self.add_weight(name="bias",
                                    shape=(input_shape[-1],),
                                    initializer='zeros',
                                    trainable=True)
        super(RoundLayer, self).build(input_shape)

    def call(self, x):
        # Use tf.matmul for dot product between `x` and `self.kernel`
        x = tf.matmul(x, self.kernel) + self.bias
        rounded_x = tf.round(x)  # Direct rounding
        return self.activation(rounded_x)

    def compute_output_shape(self, input_shape):
        return input_shape

    def get_config(self):
        config = super().get_config().copy()
        config.update({
            'activation': tf.keras.activations.serialize(self.activation)
        })
        return config


# If you intend to use `round_tensor_with_grad`, ensure it's utilized in a method within RoundLayer.
@tf.custom_gradient
def round_tensor_with_grad(x):
    def grad(dy):
        return dy  # Identity gradient

    return tf.round(x), grad


class CustomActivation(tf.keras.layers.Layer):
    def __init__(self, threshold=0.5):
        super(CustomActivation, self).__init__()
        self.threshold = threshold

    def custom_activation(self, inputs):
        return tf.where(inputs > self.threshold, tf.ones_like(inputs), tf.zeros_like(inputs))

    def call(self, inputs):
        return self.custom_activation(inputs)

    def gradient(self, inputs):
        greater_than_threshold = tf.cast(inputs > self.threshold, dtype=tf.float32)
        less_than_one = tf.cast(inputs < 1, dtype=tf.float32)
        return greater_than_threshold * less_than_one

    def compute_output_shape(self, input_shape):
        return input_shape

    def get_config(self):
        config = {"name": self.__class__.__name__}
        base_config = super(CustomActivation, self).get_config()
        return dict(list(base_config.items()) + list(config.items()))


class BinaryLayer(tf.keras.layers.Layer):
    def __init__(self, threshold=0.5):
        super(BinaryLayer, self).__init__()
        self.threshold = threshold

    def build(self, input_shape):
        # No trainable parameters to be defined
        pass

    def call(self, inputs):
        binary_values = tf.cast(inputs >= self.threshold, dtype=tf.float32)
        return binary_values


class CustomLayer_(tf.keras.layers.Layer):
    def __init__(self):
        super(CustomLayer, self).__init__()

    def build(self, input_shape):
        pass

    def call(self, inputs):
        return self.hard_sigmoid(inputs)

    def hard_sigmoid(self, x):
        return tf.maximum(0.0, tf.minimum(1.0, 0.5 * x) + 0.5)
import tensorflow.keras.backend as K
def steep_sigmoid(x, steepness=10):
    """ A sigmoid function that is steeper than the normal one, causing it to approach 0 or 1 more quickly. """
    return K.sigmoid(steepness * x)

class ExtremeActivationLayer(layers.Layer):
    def __init__(self, steepness=10):
        super(ExtremeActivationLayer, self).__init__()
        self.steepness = steepness

    def call(self, inputs):
        return steep_sigmoid(inputs, self.steepness)


def custom_activation(x):
    return tf.math.round(tf.nn.sigmoid(x))

class CustomMappingLayer(Layer):
    def __init__(self, **kwargs):
        super(CustomMappingLayer, self).__init__(**kwargs)

    def call(self, inputs):
        # Apply the mapping function
        outputs = tf.where(inputs < 0.5, 0.2 * inputs, 0.8 * inputs + 0.1)
        return outputs

    def compute_output_shape(self, input_shape):
        return input_shape
def autoencoder(input_shape, encoding_dim):
    # --- Encoding Part ---
    input_data = layers.Input(shape=input_shape)
    encoded = layers.Dense(512, activation='gelu')(input_data)
    #encoded = layers.Dropout(0.5)(encoded)
    encoded = layers.BatchNormalization()(encoded)
    encoded = layers.Dense(256, activation='relu')(encoded)
    encoded = layers.BatchNormalization()(encoded)
    encoded = layers.Dense(encoding_dim, activation='relu')(encoded)

    # --- Decoding part ---
    decoded = layers.Dense(256, activation='relu')(encoded)
    decoded = layers.BatchNormalization()(decoded)
    decoded = layers.Dense(512, activation='relu')(decoded)
    decoded = layers.BatchNormalization()(decoded)
    decoded = layers.Dense(input_shape[0], activation='sigmoid')(decoded)

    # Defining the models
    autoencoder_model = models.Model(input_data, decoded)  # Complete autoencoder = encoder + decoder
    encoder = models.Model(input_data, encoded)  # Just the encoder part

    # Now the decoder part
    encoded_input = layers.Input(shape=(encoding_dim,))
    decoder_layers = autoencoder_model.layers[-5:]  # Last 3 layers = decoder
    decoder = encoded_input
    for layer in decoder_layers:
        decoder = layer(decoder)
    decoder = models.Model(encoded_input, decoder)

    return autoencoder_model, encoder, decoder
def autoencoder_(input_shape, encoding_dim):
    # --- Encoding Part ---
    input_data = layers.Input(shape=input_shape)
    encoded = input_data
    # encoded = layers.BatchNormalization()(input_data)
    # encoded = layers.Dense(64, activation='gelu')(encoded)
    # #encoded = layers.Dropout(0.5)(encoded)
    # encoded = layers.BatchNormalization()(encoded)
    # encoded = layers.Dense(64, activation='gelu')(encoded)
    # encoded = layers.BatchNormalization()(encoded)
    # encoded = layers.Dense(32, activation='relu')(encoded)
    # encoded = layers.BatchNormalization()(encoded)
    # encoded = layers.Dense(32, activation='relu')(encoded)
    # encoded = layers.BatchNormalization()(encoded)
    # encoded = layers.Dense(16, activation='relu')(encoded)
    # encoded = layers.BatchNormalization()(encoded)
    # encoded = layers.Dense(16, activation='relu')(encoded)
    # encoded = layers.BatchNormalization()(encoded)
    encoded = layers.Dense(16, activation='relu')(encoded)
    #encoded = layers.BatchNormalization()(encoded)
    encoded = layers.Dense(8, activation='relu')(encoded)
    #encoded = layers.BatchNormalization()(encoded)
    encoded = layers.Dense(encoding_dim, activation='relu')(encoded)
    #encoded = CustomActivation()(encoded)
    # --- Decoding part ---
    decoded = layers.Dense(8, activation='relu')(encoded)
    # decoded = layers.BatchNormalization()(decoded)
    decoded = layers.Dense(16, activation='relu')(decoded)
    #decoded = layers.BatchNormalization()(decoded)
    # decoded = layers.Dense(8, activation='relu')(decoded)
    # decoded = layers.BatchNormalization()(decoded)
    # decoded = layers.Dense(16, activation='relu')(decoded)
    # decoded = layers.BatchNormalization()(decoded)
    # decoded = layers.Dense(16, activation='relu')(decoded)
    # decoded = layers.BatchNormalization()(decoded)
    # decoded = layers.Dense(32, activation='relu')(decoded)
    # decoded = layers.BatchNormalization()(decoded)
    # decoded = layers.Dense(32, activation='relu')(decoded)
    # decoded = layers.BatchNormalization()(decoded)
    # decoded = layers.Dense(64, activation='relu')(decoded)
    # decoded = layers.BatchNormalization()(decoded)
    # decoded = layers.Dense(64, activation='relu')(decoded)
    # decoded = layers.BatchNormalization()(decoded)
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
        self.meanLoss = []
        self.count = 0

    def on_epoch_end(self, epoch, logs=None):
        if (epoch + 1) % 1 == 0:
            self.loss.append(logs['loss'])
            self.val_loss.append(logs['val_loss'])

        if (epoch + 1) % 100 == 0:  # Adjust this to calculate trend line every n epochs
            # Calculate trend line
            epoch_numbers = np.arange(len(self.loss)).reshape(-1, 1)
            from sklearn.linear_model import LinearRegression
            model = LinearRegression()
            model.fit(epoch_numbers, self.loss)
            trend_line = model.predict(epoch_numbers)

            # Plot trend line (optional)
            plt.plot(epoch_numbers, trend_line, color='red')
            plt.xlabel('Epochs')
            plt.ylabel('Trend')
            plt.title('Trend vs. Epochs')
            plt.legend()
            plt.grid(True)
            plt.show()

        # if (epoch + 1) % 100 == 0:
        #     # Plot the loss
        #     plt.plot(self.loss, label='Training Loss')
        #     plt.plot(self.val_loss, label='Validation Loss')
        #     plt.xlabel('Epochs')
        #     plt.ylabel('Loss')
        #     plt.title('Loss vs. Epochs')
        #     plt.legend()
        #     plt.grid(True)
        #     plt.show()
        if (epoch + 1) % 10 == 0:
            # Save the encoder model
            autoencoder_model.save_weights('autoencoder_model_zip.weights.h5')
            encoder.save_weights('encoder_model_zip.weights.h5')

            # Save the decoder weights
            decoder.save_weights('decoder_weights_binary.weights.h5')

        if epoch % 10000 == 0:
            self.loss = []
            self.val_loss = []
        if logs['loss'] <= self.threshold:
            print(f"\nReached loss threshold of {self.threshold}. Stopping training.")

            # Save the encoder model
            autoencoder_model.save_weights('autoencoder_model_zip.weights.h5')
            encoder.save_weights('encoder_model_zip.weights.h5')

            # Save the decoder weights
            decoder.save_weights('decoder_weights_binary.weights.h5')
            self.model.stop_training = True

        if (epoch + 1) % 10 == 0:
            #
            # # Generate synthetic data
            # num_samples = 10096
            # data = np.random.randint(2, size=(num_samples, *input_shape))  # Generate random 0s and 1s

            # Test the encoder and decoder with the test data
            test_encoded_data = encoder.predict(data)
            test_decoded_data = decoder.predict(np.round(test_encoded_data))

            # Check if original data and reconstructed data are the same
            if np.array_equal(data, np.round(test_decoded_data)):
                print("Original data and Reconstructed data are the same.")

                # Save the encoder model
                autoencoder_model.save_weights('autoencoder_model_zip.weights.h5')
                encoder.save_weights('encoder_model_zip.weights.h5')

                # Save the decoder weights
                decoder.save_weights('decoder_weights_binary.weights.h5')
                if self.count == 0:
                    self.model.stop_training = True
                self.count += 1
            else:
                self.count = 0
                print("Original data and Reconstructed data are different.")
            # Test the encoder and decoder with the test data
            test_encoded_data = encoder.predict(data)
            test_decoded_data = decoder.predict(test_encoded_data)

            # Check if original data and reconstructed data are the same
            if np.array_equal(data, np.round(test_decoded_data)):
                print("Original data and Reconstructed data are the same.")

            else:

                print("Original data and Reconstructed data are different.")


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
        padded_chunk = np.pad(remainder_chunk, (0, chunk_size - remainder), mode='constant', constant_values=6)
        chunks.append(padded_chunk)
    return chunks


# Define your input_shape and encoding_dim
input_shape = (8,)  # Assuming input data size of 8
encoding_dim = 1  # Adjust the encoding dimension as needed

# Generate synthetic data
num_samples = (10000)
data = np.random.randint(2, size=(num_samples, *input_shape), dtype=np.int8)  # Generate random 0s and 1s

# Split data into training and validation sets
validation_split = 0.3
num_validation_samples = int(num_samples * validation_split)
x_train = data[num_validation_samples:]
x_val = data[:num_validation_samples]

autoencoder_model, encoder, decoder = autoencoder(input_shape, encoding_dim)

threshold_callback = ThresholdCallback(threshold=0.00001)

# compile model
#autoencoder_model.compile(loss='', optimizer=tf.keras.optimizers.Adam(learning_rate=1e-8), metrics='accuracy')
autoencoder_model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-6),
                          loss=tf.keras.losses.BinaryCrossentropy(),
                          metrics=tf.keras.metrics.BinaryAccuracy())
#autoencoder_model.compile(optimizer='adam', loss='categorical_crossentropy')

# Loading saved models
if os.path.exists('encoder_model_zip.weights.h5') and os.path.exists('decoder_weights_binary.weights.h5'):
    autoencoder_model.load_weights('autoencoder_model_zip.weights.h5')
    encoder.load_weights('encoder_model_zip.weights.h5')

    decoder.load_weights('decoder_weights_binary.weights.h5')

    data = np.load('data.npy')

    #decoder_8.load_weights('decoder_weights_binary.weights-BatchNorm-8-3.h5')
    # Load your test data here
    # For demonstration, let's assume you have test_data

    # Test the encoder and decoder with the test data
    # test_encoded_data = encoder.predict(data)
    # test_decoded_data = decoder.predict(np.round(test_encoded_data))
    #
    # # Check if original data and reconstructed data are the same
    # if np.array_equal(data, np.round(test_decoded_data)):
    #     print("Original data and Reconstructed data are the same.")
    # else:
    #     print("Original data and Reconstructed data are different.")
else:
    np.save('data.npy', data)

    print("No saved models found.")

# Split data into training and validation sets
validation_split = 0.3
num_validation_samples = int(num_samples * validation_split)
x_train = data[num_validation_samples:]
x_val = data[:num_validation_samples]

# Train the model with validation data
history = autoencoder_model.fit(x_train, x_train, epochs=100000000, shuffle=True, batch_size=64,
                                validation_data=(x_val, x_val),
                                callbacks=[threshold_callback])

# Encode and decode the data
encoded_data = encoder.predict(data)
decoded_data = decoder.predict(np.round(encoded_data))

# Check if original data and reconstructed data are the same
if np.array_equal(data, np.round(decoded_data)):
    print("Original data and Reconstructed data are the same.")

else:
    print("Original data and Reconstructed data are different.")

# Save the encoder model
encoder.save_weights('encoder_model_zip.weights.h5')
autoencoder_model.save_weights('autoencoder_model_zip.weights.h5')
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

# Function to remove padding from reconstructed data
# def remove_padding(reconstructed_data, original_lengths):
#     reconstructed_data_trimmed = []
#     start_index = 0
#     for length in original_lengths:
#         reconstructed_data_trimmed.append(reconstructed_data[start_index:start_index + length])
#         start_index += length
#     return np.concatenate(reconstructed_data_trimmed)


# Load your PDF file as binary data
filename = "test"
with open(filename, 'rb') as obj:
    binary_data = obj.read()


#

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

# Assume compressed_data is ready and scaled appropriately
# Convert to uint8 if not already done. This is necessary for byte conversion.
compressed_data = np.array(compressed_data)
compressed_data_uint8 = compressed_data.astype(np.uint8)

# Convert to bytes
compressed_data_bytes = compressed_data_uint8.tobytes()
# Write to binary file
with open('compressed_data.bin', 'wb') as file:
    file.write(compressed_data_bytes)
# Load the compressed binary AI file
with open('compressed_data.bin', 'rb') as file:
    compressed_data_bytes = file.read()

# Load the decoder model
decoder.load_weights('decoder_weights_binary.weights.h5')
# Decode the compressed data to obtain the original data
original_data = []
reconstructed_data = []


def reconstruct_data(chunks):
    """Reconstruct the data from the list of padded chunks."""
    # Concatenate the padded chunks
    #padded_sequence = np.concatenate(chunks)
    # Find the index of the last element that is not equal to the padding value (-1)
    last_nonpadding_index = np.where(chunks != 6)[0][-1]
    # Remove padding from the concatenated sequence
    original_sequence = chunks[:last_nonpadding_index + 1]
    #original_sequence = padded_sequence[:8]
    return original_sequence


#


# Convert compressed data bytes back to numpy array of uint8
compressed_data_uint8 = np.frombuffer(compressed_data_bytes, dtype=np.uint8)

# Reshape the compressed data to the shape of (num_chunks, 4)
num_chunks = len(compressed_data_uint8) // encoding_dim
compressed_data = compressed_data_uint8[:num_chunks * encoding_dim].reshape((num_chunks, encoding_dim))
autoencoder_model, encoder, decoder = autoencoder(input_shape, encoding_dim)

# Load the decoder model
decoder.load_weights('decoder_weights_binary.weights.h5')
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
    #reconstructed_chunk = remove_padding(reconstructed_chunk.squeeze(), [input_shape[0]])
    reconstructed_chunk = reconstructed_chunk.squeeze()
    reconstructed_data.append(reconstructed_chunk)  # Remove batch dimension

    # Store original length of chunk
    # original_lengths.append(len(chunk[0]))

# Convert the reconstructed data from uint8 back to binary (0s and 1s) before saving
reconstructed_data = np.round(reconstructed_data, 0)  # Convert probabilities to binary
reconstructed_data = reconstructed_data.astype(np.uint8)

# Convert the numpy arrays in reconstructed_data to binary strings
reconstructed_data = [''.join(map(str, map(int, b))) for b in reconstructed_data]


def chunk_string(string, size):
    return [string[i:i + size] for i in range(0, len(string), size)]


reconstructed_data_bit_chunks = [chunk_string(b, 8) for b in reconstructed_data]

byte_array = bytearray([int(b, 2) for sublist in reconstructed_data_bit_chunks for b in sublist])

with open("reconstructed_binary_file", "wb") as f:
    f.write(byte_array)

print("Reconstructed binary file saved.")
