import tensorflow as tf
from tensorflow.keras import layers, models, callbacks
import numpy as np
import os
import matplotlib.pyplot as plt
def autoencoder(input_shape, encoding_dim):
    input_data = layers.Input(shape=input_shape)
    encoded = layers.Dense(512, activation='relu')(input_data)
    encoded = layers.Dropout(0.3)(encoded)  # Dropout layer with rate 0.5
    encoded = layers.Dense(encoding_dim, activation='sigmoid')(encoded)
    encoded = layers.Dense(encoding_dim, activation='relu')(encoded)
    encoded = layers.Dropout(0.3)(encoded)  # Dropout layer with rate 0.5
    encoded = layers.Dense(encoding_dim, activation='sigmoid')(encoded)

    # At this point the representation is (encoding_dim)-dimensional
    decoded = layers.Dense(512, activation='sigmoid')(encoded)
    decoded = layers.Dense(512, activation='relu')(decoded)
    decoded = layers.Dense(512, activation='sigmoid')(decoded)
    decoded = layers.Dropout(0.3)(decoded)  # Dropout layer with rate 0.5
    decoded = layers.Dense(input_shape[0], activation='relu')(decoded)

    # This model maps an input to its reconstruction
    autoencoder_model = models.Model(input_data, decoded)

    # This model maps an input to its encoded representation
    encoder = models.Model(input_data, encoded)

    # create a placeholder for an encoded (encoding_dim-dimensional) input
    encoded_input = layers.Input(shape=(encoding_dim,))

    # retrieve the layers of the autoencoder model
    decoder_layer1 = autoencoder_model.layers[-5]  # added this line
    decoder_layer2 = autoencoder_model.layers[-4]  # added this line
    decoder_layer3 = autoencoder_model.layers[-3]
    decoder_layer4 = autoencoder_model.layers[-2]
    decoder_layer5 = autoencoder_model.layers[-1]

    # create the decoder model
    decoder_output = decoder_layer5(decoder_layer4(decoder_layer3(decoder_layer2(decoder_layer1(encoded_input)))))
    decoder = models.Model(encoded_input, decoder_output)

    return autoencoder_model, encoder, decoder

val_loss = []
loss = []
# Define custom callback to stop training if loss falls below a threshold
class ThresholdCallback(callbacks.Callback):
    def __init__(self, threshold):
        super(ThresholdCallback, self).__init__()
        self.threshold = threshold

    def on_epoch_end(self, epoch, logs=None):
        loss.append(logs['loss'])
        val_loss.append(logs['val_loss'])
        if epoch % 50 == 0:
            # Plot the loss
            plt.plot(loss, label='Training Loss')
            plt.plot(val_loss, label='Validation Loss')
            plt.xlabel('Epochs')
            plt.ylabel('Loss')
            plt.title('Loss vs. Epochs')
            plt.legend()
            plt.grid(True)
            plt.show()
        if logs['loss'] <= self.threshold:
            print(f"\nReached loss threshold of {self.threshold}. Stopping training.")
            self.model.stop_training = True


# Define your input_shape and encoding_dim
input_shape = (1024,)  # Assuming input data size of 1024
encoding_dim = 768  # Adjust the encoding dimension as needed

# Generate synthetic data
num_samples = 2000
data = np.random.binomial(1, 0.5, size=(num_samples, *input_shape))

# Split data into training and validation sets
validation_split = 0.2
num_validation_samples = int(num_samples * validation_split)
x_train = data[num_validation_samples:]
x_val = data[:num_validation_samples]

autoencoder_model, encoder, decoder = autoencoder(input_shape, encoding_dim)

if os.path.exists('encoder_model_zip.keras'):
    encoder = models.load_model('encoder_model_zip.keras')
    decoder = models.load_model('decoder_model_zip.keras')

    shape = data.shape
    dtype = data.dtype

    with open("data.bin", "rb") as f:
        loaded_data = np.frombuffer(f.read(), dtype=dtype)
        data = loaded_data.reshape(shape)  # Original shape
    f.close()
    print("Loaded existing model.")
else:
    threshold_callback = ThresholdCallback(threshold=0.01)
    autoencoder_model.compile(optimizer='adam', loss='binary_crossentropy')

    with open('data.bin', 'wb') as f:
        f.write(data.tobytes())
    f.close()

    # Train the model with validation data
    history = autoencoder_model.fit(x_train, x_train, epochs=10000, batch_size=64,
                                    validation_data=(x_val, x_val),
                                    callbacks=[threshold_callback])

    encoder.save('encoder_model_zip.keras')
    decoder.save('decoder_model_zip.keras')


# FIX: compute encoded and decoded data
encoded_data = encoder.predict(data)
decoded_data = decoder.predict(encoded_data)  # Reconstructed data

# Check if original data and reconstructed data are the same
if np.array_equal(data, np.round(decoded_data)):
    print("Original data and Reconstructed data are the same.")
else:
    print("Original data and Reconstructed data are different.")
