import numpy as np
import matplotlib.pyplot as plt
import pickle
import os


def adam_optimizer(weights, biases, dw, db, prev_m_w, prev_v_w, prev_m_b, prev_v_b, learning_rate, beta1=0.95, beta2=0.999, epsilon=1e-8, t=1):
    m_w = beta1 * prev_m_w + (1 - beta1) * dw
    v_w = beta2 * prev_v_w + (1 - beta2) * (dw ** 2)

    m_b = beta1 * prev_m_b + (1 - beta1) * db
    v_b = beta2 * prev_v_b + (1 - beta2) * (db ** 2)

    m_hat_w = m_w / (1 - beta1 ** t)
    v_hat_w = v_w / (1 - beta2 ** t)
    m_hat_b = m_b / (1 - beta1 ** t)
    v_hat_b = v_b / (1 - beta2 ** t)

    weights -= learning_rate * m_hat_w / (np.sqrt(v_hat_w) + epsilon)
    biases -= learning_rate * m_hat_b / (np.sqrt(v_hat_b) + epsilon)

    return weights, biases, m_w, v_w, m_b, v_b

class ActivationLayer:
    def __init__(self, activation_function, activation_derivative):
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.input = None

    def forward(self, input_data):
        self.input = input_data
        return self.activation_function(input_data)

    def backward(self, delta):
        return delta * self.activation_derivative(self.input)

def load_model(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            saved_data = pickle.load(f)
            model = saved_data['model']
            x_train = saved_data['x_train']
            x_val = saved_data['x_val']
            return model, x_train, x_val
    return None, None, None

def save_model(model, x_train, x_val, filename):
    saved_data = {'model': model, 'x_train': x_train, 'x_val': x_val}
    with open(filename, 'wb') as f:
        pickle.dump(saved_data, f)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_(x):
    """ Compute sigmoid for x avoiding overflow. """
    # When x is too large, exp(-x) will be close to 0, so we can approximate sigmoid(x) as 1
    return np.where(x >= 0,
                    1 / (1 + np.exp(-x)),
                    np.exp(x) / (1 + np.exp(x)))

def sigmoid_derivative(output):
    return output * (1 - output)

def relu(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x <= 0, 0, 1)

def gelu(x):
    return x * 0.5 * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3))))

def gelu_derivative(x):
    return 0.5 * (1 + np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3)))) + \
           (0.5 * x * (1 - np.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * np.power(x, 3)))) * \
            (1 + np.sqrt(2 / np.pi) * (0.044715 * np.power(x, 3) + 3 * 0.044715 * np.power(x, 2))))

def batchnorm(x, gamma, beta, epsilon=1e-5):
    # Compute mean and variance along the batch dimension
    mean = np.mean(x, axis=0, keepdims=True)
    variance = np.var(x, axis=0, keepdims=True)
    # Normalize input data
    x_norm = (x - mean) / np.sqrt(variance + epsilon)
    # Scale and shift the normalized input
    return gamma * x_norm + beta, x_norm, mean, variance

def binary_to_bit_array(binary_data):
    return np.unpackbits(np.frombuffer(binary_data, dtype=np.uint8))

def remove_padding(reconstructed_data, original_lengths):
    reconstructed_data_trimmed = []
    start_index = 0
    for length in original_lengths:
        reconstructed_data_trimmed.append(reconstructed_data[start_index:start_index + length])
        start_index += length
    return np.concatenate(reconstructed_data_trimmed)

def chunk_data(bit_sequence, chunk_size):
    num_chunks = len(bit_sequence) // chunk_size
    remainder = len(bit_sequence) % chunk_size
    chunks = [bit_sequence[i * chunk_size: (i + 1) * chunk_size] for i in range(num_chunks)]
    if remainder > 0:
        remainder_chunk = bit_sequence[-remainder:]
        padded_chunk = np.pad(remainder_chunk, (0, chunk_size - remainder), mode='constant', constant_values=0)
        chunks.append(padded_chunk)
    return chunks
import os
import numpy as np
import matplotlib.pyplot as plt

def train_autoencoder(x_train, x_val, encoder_weights0, encoder_bias0, encoder_weights1, encoder_bias1, encoder_weights2, encoder_bias2, decoder_weights1, decoder_bias1, decoder_weights2, decoder_bias2, decoder_weights3, decoder_bias3, gamma0, beta0, gamma1, beta1, gamma2, beta2, learning_rate, num_epochs, m_encoder_weights0, v_encoder_weights0, m_encoder_bias0, v_encoder_bias0, m_encoder_weights1, v_encoder_weights1, m_encoder_bias1, v_encoder_bias1, m_encoder_weights2, v_encoder_weights2, m_encoder_bias2, v_encoder_bias2, m_decoder_weights1, v_decoder_weights1, m_decoder_bias1, v_decoder_bias1, m_decoder_weights2, v_decoder_weights2, m_decoder_bias2, v_decoder_bias2, m_decoder_weights3, v_decoder_weights3, m_decoder_bias3, v_decoder_bias3):
    train_losses = []
    val_losses = []

    for epoch in range(num_epochs):
        # Forward pass
        encoder_output0 = sigmoid(np.dot(x_train, encoder_weights0) + encoder_bias0)
        encoder_output0_bn, _, _, _ = batchnorm(encoder_output0, gamma0, beta0)
        encoder_output1 = sigmoid(np.dot(encoder_output0_bn, encoder_weights1) + encoder_bias1)
        encoder_output1_bn, _, _, _ = batchnorm(encoder_output1, gamma1, beta1)
        encoded = np.round(sigmoid(np.dot(encoder_output1_bn, encoder_weights2) + encoder_bias2))
        encoded_bn, _, _, _ = batchnorm(encoded, gamma2, beta2)

        decoder_output1 = sigmoid(np.dot(encoded_bn, decoder_weights1) + decoder_bias1)
        decoder_output2 = sigmoid(np.dot(decoder_output1, decoder_weights2) + decoder_bias2)
        decoded = sigmoid(np.dot(decoder_output2, decoder_weights3) + decoder_bias3)

        # Calculate training loss
        train_loss = np.mean(np.abs(x_train - decoded))
        train_losses.append(train_loss)
        encoder_output_val0 = sigmoid(np.dot(x_val, encoder_weights0) + encoder_bias0)
        encoder_output_val0_bn, _, _, _ = batchnorm(encoder_output_val0, gamma0, beta0)
        encoder_output_val1 = sigmoid(np.dot(encoder_output_val0_bn, encoder_weights1) + encoder_bias1)
        encoder_output_val1_bn, _, _, _ = batchnorm(encoder_output_val1, gamma1, beta1)
        encoded_val = np.round(sigmoid(np.dot(encoder_output_val1_bn, encoder_weights2) + encoder_bias2))
        encoded_val_bn, _, _, _ = batchnorm(encoded_val, gamma2, beta2)

        decoder_output_val1 = sigmoid(np.dot(encoded_val_bn, decoder_weights1) + decoder_bias1)
        decoder_output_val2 = sigmoid(np.dot(decoder_output_val1, decoder_weights2) + decoder_bias2)
        decoded_val = sigmoid(np.dot(decoder_output_val2, decoder_weights3) + decoder_bias3)

        val_loss = np.mean(np.abs(x_val - decoded_val))
        val_losses.append(val_loss)

        # Backpropagation
        decoder_error = x_train - decoded
        decoder_delta3 = decoder_error * sigmoid_derivative(decoded)
        decoder_error2 = decoder_delta3.dot(decoder_weights3.T)
        decoder_delta2 = decoder_error2 * sigmoid_derivative(decoder_output2)
        decoder_error1 = decoder_delta2.dot(decoder_weights2.T)
        decoder_delta1 = decoder_error1 * sigmoid_derivative(decoder_output1)

        encoder_error2 = decoder_delta1.dot(decoder_weights1.T)
        encoder_delta2 = encoder_error2 * sigmoid_derivative(encoded)

        encoder_error1 = encoder_delta2.dot(encoder_weights2.T)
        encoder_delta1 = encoder_error1 * sigmoid_derivative(encoder_output1)

        encoder_error0 = encoder_delta1.dot(encoder_weights1.T)
        encoder_delta0 = encoder_error0 * sigmoid_derivative(encoder_output0)
        # Update weights and biases
        decoder_weights3 += decoder_output2.T.dot(decoder_delta3) * learning_rate
        decoder_bias3 += np.sum(decoder_delta3, axis=0) * learning_rate
        decoder_weights2 += decoder_output1.T.dot(decoder_delta2) * learning_rate
        decoder_bias2 += np.sum(decoder_delta2, axis=0) * learning_rate
        decoder_weights1 += encoded.T.dot(decoder_delta1) * learning_rate
        decoder_bias1 += np.sum(decoder_delta1, axis=0) * learning_rate

        encoder_weights2 += encoder_output1.T.dot(encoder_delta2) * learning_rate
        encoder_bias2 += np.sum(encoder_delta2, axis=0) * learning_rate
        encoder_weights1 += encoder_output0.T.dot(encoder_delta1) * learning_rate
        encoder_bias1 += np.sum(encoder_delta1, axis=0) * learning_rate
        encoder_weights0 += x_train.T.dot(encoder_delta0) * learning_rate
        encoder_bias0 += np.sum(encoder_delta0, axis=0) * learning_rate
        # Update weights and biases using Adam optimizer for other parameters
        # encoder_weights2, encoder_bias2, m_encoder_weights2, v_encoder_weights2, m_encoder_bias2, v_encoder_bias2 = adam_optimizer(
        #     encoder_weights2, encoder_bias2,
        #     encoder_output1_bn.T.dot(encoder_delta2),
        #     np.sum(encoder_delta2, axis=0),
        #     m_encoder_weights2, v_encoder_weights2, m_encoder_bias2, v_encoder_bias2,
        #     learning_rate, t=epoch + 1)
        #
        # encoder_weights1, encoder_bias1, m_encoder_weights1, v_encoder_weights1, m_encoder_bias1, v_encoder_bias1 = adam_optimizer(
        #     encoder_weights1, encoder_bias1,
        #     encoder_output0_bn.T.dot(encoder_delta1),
        #     np.sum(encoder_delta1, axis=0),
        #     m_encoder_weights1, v_encoder_weights1, m_encoder_bias1, v_encoder_bias1,
        #     learning_rate, t=epoch + 1)
        #
        # encoder_weights0, encoder_bias0, m_encoder_weights0, v_encoder_weights0, m_encoder_bias0, v_encoder_bias0 = adam_optimizer(
        #     encoder_weights0, encoder_bias0,
        #     x_train.T.dot(encoder_delta0),
        #     np.sum(encoder_delta0, axis=0),
        #     m_encoder_weights0, v_encoder_weights0, m_encoder_bias0, v_encoder_bias0,
        #     learning_rate, t=epoch + 1)
        #
        # decoder_weights3, decoder_bias3, m_decoder_weights3, v_decoder_weights3, m_decoder_bias3, v_decoder_bias3 = adam_optimizer(
        #     decoder_weights3, decoder_bias3,
        #     decoder_output2.T.dot(decoder_delta3),
        #     np.sum(decoder_delta3, axis=0),
        #     m_decoder_weights3, v_decoder_weights3, m_decoder_bias3, v_decoder_bias3,
        #     learning_rate, t=epoch + 1)
        #
        # decoder_weights2, decoder_bias2, m_decoder_weights2, v_decoder_weights2, m_decoder_bias2, v_decoder_bias2 = adam_optimizer(
        #     decoder_weights2, decoder_bias2,
        #     decoder_output1.T.dot(decoder_delta2),
        #     np.sum(decoder_delta2, axis=0),
        #     m_decoder_weights2, v_decoder_weights2, m_decoder_bias2, v_decoder_bias2,
        #     learning_rate, t=epoch + 1)
        #
        # decoder_weights1, decoder_bias1, m_decoder_weights1, v_decoder_weights1, m_decoder_bias1, v_decoder_bias1 = adam_optimizer(
        #     decoder_weights1, decoder_bias1,
        #     encoded_bn.T.dot(decoder_delta1),
        #     np.sum(decoder_delta1, axis=0),
        #     m_decoder_weights1, v_decoder_weights1, m_decoder_bias1, v_decoder_bias1,
        #     learning_rate, t=epoch + 1)
        # Apply learning rate decay
        #learning_rate /= (epoch + 1)
        # Calculate accuracy
        # Considering exact reconstruction as success

        # Calculate accuracy
        # Comparing each sample in the validation set
        accurate_reconstructions = np.round(decoded_val) == x_val
        accuracy = np.mean(accurate_reconstructions)

        # Print progress
        # Print accuracy along with loss
        if epoch % 100 == 0:
            print(f"Epoch {epoch}: Training Loss: {train_loss}, Validation Loss: {val_loss}, Accuracy: {accuracy * 100:.6f}%")


            # Save the trained model
            model = {
                'encoder_weights0': encoder_weights0,
                'encoder_bias0': encoder_bias0,
                'encoder_weights1': encoder_weights1,
                'encoder_bias1': encoder_bias1,
                'encoder_weights2': encoder_weights2,
                'encoder_bias2': encoder_bias2,
                'decoder_weights1': decoder_weights1,
                'decoder_bias1': decoder_bias1,
                'decoder_weights2': decoder_weights2,
                'decoder_bias2': decoder_bias2,
                'decoder_weights3': decoder_weights3,
                'decoder_bias3': decoder_bias3,
                'm_encoder_weights0': m_encoder_weights0,
                'v_encoder_weights0': v_encoder_weights0,
                'm_encoder_bias0': m_encoder_bias0,
                'v_encoder_bias0': v_encoder_bias0,
                'm_encoder_weights1': m_encoder_weights1,
                'v_encoder_weights1': v_encoder_weights1,
                'm_encoder_bias1': m_encoder_bias1,
                'v_encoder_bias1': v_encoder_bias1,
                'm_encoder_weights2': m_encoder_weights2,
                'v_encoder_weights2': v_encoder_weights2,
                'm_encoder_bias2': m_encoder_bias2,
                'v_encoder_bias2': v_encoder_bias2,
                'm_decoder_weights1': m_decoder_weights1,
                'v_decoder_weights1': v_decoder_weights1,
                'm_decoder_bias1': m_decoder_bias1,
                'v_decoder_bias1': v_decoder_bias1,
                'm_decoder_weights2': m_decoder_weights2,
                'v_decoder_weights2': v_decoder_weights2,
                'm_decoder_bias2': m_decoder_bias2,
                'v_decoder_bias2': v_decoder_bias2,
                'm_decoder_weights3': m_decoder_weights3,
                'v_decoder_weights3': v_decoder_weights3,
                'm_decoder_bias3': m_decoder_bias3,
                'v_decoder_bias3': v_decoder_bias3
            }
            # Save the trained model along with training set
            save_model(model, x_train, x_val, 'autoencoder_model.pkl')
            # This will close the currently active plot
            plt.close('all')
            # Plot training and validation losses
            plt.figure(figsize=(5, 5))
            plt.plot(train_losses, label='Training Loss')
            plt.plot(val_losses, label='Validation Loss')
            plt.xlabel('Epoch')
            plt.ylabel('Loss')
            plt.title('Training and Validation Losses')
            plt.legend()
            plt.show()

            # Check if original data equals reconstructed data rounded
            if np.array_equal(x_train, np.round(decoded)):
                print(f"Original data equals reconstructed data rounded at epoch {epoch}. Stopping training.")
                break

def main():
    # Define architecture and parameters
    num_samples = 8200
    num_features = 8
    split_ratio = 0.8
    learning_rate = 1e-4
    num_epochs = 100000
    chunk_size = 8

    # Generate sample data
    data = np.random.randint(0, 2, size=(num_samples, num_features))

    # Split data into training and validation sets
    split_index = int(num_samples * split_ratio)
    x_train = data[:split_index]
    x_val = data[split_index:]

    input_size = num_features
    encoder_hidden_size0 = 64
    encoder_hidden_size1 = 32
    encoder_hidden_size2 = 8*2
    decoder_hidden_size1 = 32
    decoder_hidden_size2 = 64
    output_size = input_size

    # Initialize weights and biases
    if os.path.exists('autoencoder_model.pkl'):
        model, x_train, x_val = load_model('autoencoder_model.pkl')
        encoder_weights0 = model['encoder_weights0']
        encoder_bias0 = model['encoder_bias0']
        encoder_weights1 = model['encoder_weights1']
        encoder_bias1 = model['encoder_bias1']
        encoder_weights2 = model['encoder_weights2']
        encoder_bias2 = model['encoder_bias2']
        decoder_weights1 = model['decoder_weights1']
        decoder_bias1 = model['decoder_bias1']
        decoder_weights2 = model['decoder_weights2']
        decoder_bias2 = model['decoder_bias2']
        decoder_weights3 = model['decoder_weights3']
        decoder_bias3 = model['decoder_bias3']
        m_encoder_weights0 = model['m_encoder_weights0']
        v_encoder_weights0 = model['v_encoder_weights0']
        m_encoder_bias0 = model['m_encoder_bias0']
        v_encoder_bias0 = model['v_encoder_bias0']

        m_encoder_weights1 = model['m_encoder_weights1']
        v_encoder_weights1 = model['v_encoder_weights1']
        m_encoder_bias1 = model['m_encoder_bias1']
        v_encoder_bias1 = model['v_encoder_bias1']

        m_encoder_weights2 = model['m_encoder_weights2']
        v_encoder_weights2 = model['v_encoder_weights2']
        m_encoder_bias2 = model['m_encoder_bias2']
        v_encoder_bias2 = model['v_encoder_bias2']

        m_decoder_weights1 = model['m_decoder_weights1']
        v_decoder_weights1 = model['v_decoder_weights1']
        m_decoder_bias1 = model['m_decoder_bias1']
        v_decoder_bias1 = model['v_decoder_bias1']

        m_decoder_weights2 = model['m_decoder_weights2']
        v_decoder_weights2 = model['v_decoder_weights2']
        m_decoder_bias2 = model['m_decoder_bias2']
        v_decoder_bias2 = model['v_decoder_bias2']

        m_decoder_weights3 = model['m_decoder_weights3']
        v_decoder_weights3 = model['v_decoder_weights3']
        m_decoder_bias3 = model['m_decoder_bias3']
        v_decoder_bias3 = model['v_decoder_bias3']

    else:
        encoder_weights0 = np.random.randn(input_size, encoder_hidden_size0)
        encoder_bias0 = np.zeros(encoder_hidden_size0)
        encoder_weights1 = np.random.randn(encoder_hidden_size0, encoder_hidden_size1)
        encoder_bias1 = np.zeros(encoder_hidden_size1)
        encoder_weights2 = np.random.randn(encoder_hidden_size1, encoder_hidden_size2)
        encoder_bias2 = np.zeros(encoder_hidden_size2)
        decoder_weights1 = np.random.randn(encoder_hidden_size2, decoder_hidden_size1)
        decoder_bias1 = np.zeros(decoder_hidden_size1)
        decoder_weights2 = np.random.randn(decoder_hidden_size1, decoder_hidden_size2)
        decoder_bias2 = np.zeros(decoder_hidden_size2)
        decoder_weights3 = np.random.randn(decoder_hidden_size2, output_size)
        decoder_bias3 = np.zeros(output_size)
        # Initialize moment estimates for Adam optimizer
        m_encoder_weights0 = np.zeros_like(encoder_weights0)
        v_encoder_weights0 = np.zeros_like(encoder_weights0)
        m_encoder_bias0 = np.zeros_like(encoder_bias0)
        v_encoder_bias0 = np.zeros_like(encoder_bias0)

        m_encoder_weights1 = np.zeros_like(encoder_weights1)
        v_encoder_weights1 = np.zeros_like(encoder_weights1)
        m_encoder_bias1 = np.zeros_like(encoder_bias1)
        v_encoder_bias1 = np.zeros_like(encoder_bias1)

        m_encoder_weights2 = np.zeros_like(encoder_weights2)
        v_encoder_weights2 = np.zeros_like(encoder_weights2)
        m_encoder_bias2 = np.zeros_like(encoder_bias2)
        v_encoder_bias2 = np.zeros_like(encoder_bias2)

        m_decoder_weights1 = np.zeros_like(decoder_weights1)
        v_decoder_weights1 = np.zeros_like(decoder_weights1)
        m_decoder_bias1 = np.zeros_like(decoder_bias1)
        v_decoder_bias1 = np.zeros_like(decoder_bias1)

        m_decoder_weights2 = np.zeros_like(decoder_weights2)
        v_decoder_weights2 = np.zeros_like(decoder_weights2)
        m_decoder_bias2 = np.zeros_like(decoder_bias2)
        v_decoder_bias2 = np.zeros_like(decoder_bias2)

        m_decoder_weights3 = np.zeros_like(decoder_weights3)
        v_decoder_weights3 = np.zeros_like(decoder_weights3)
        m_decoder_bias3 = np.zeros_like(decoder_bias3)
        v_decoder_bias3 = np.zeros_like(decoder_bias3)

    gamma0 = np.ones(encoder_hidden_size0)
    beta0 = np.zeros(encoder_hidden_size0)
    gamma1 = np.ones(encoder_hidden_size1)
    beta1 = np.zeros(encoder_hidden_size1)
    gamma2 = np.ones(encoder_hidden_size2)
    beta2 = np.zeros(encoder_hidden_size2)

    # Train the autoencoder
    train_autoencoder(x_train, x_val, encoder_weights0, encoder_bias0, encoder_weights1, encoder_bias1, encoder_weights2, encoder_bias2, decoder_weights1, decoder_bias1, decoder_weights2, decoder_bias2, decoder_weights3, decoder_bias3, gamma0, beta0, gamma1, beta1, gamma2, beta2, learning_rate, num_epochs, m_encoder_weights0, v_encoder_weights0, m_encoder_bias0, v_encoder_bias0, m_encoder_weights1, v_encoder_weights1, m_encoder_bias1, v_encoder_bias1, m_encoder_weights2, v_encoder_weights2, m_encoder_bias2, v_encoder_bias2, m_decoder_weights1, v_decoder_weights1, m_decoder_bias1, v_decoder_bias1, m_decoder_weights2, v_decoder_weights2, m_decoder_bias2, v_decoder_bias2, m_decoder_weights3, v_decoder_weights3, m_decoder_bias3, v_decoder_bias3)

    # Save the trained model
    model = {
        'encoder_weights0': encoder_weights0,
        'encoder_bias0': encoder_bias0,
        'encoder_weights1': encoder_weights1,
        'encoder_bias1': encoder_bias1,
        'encoder_weights2': encoder_weights2,
        'encoder_bias2': encoder_bias2,
        'decoder_weights1': decoder_weights1,
        'decoder_bias1': decoder_bias1,
        'decoder_weights2': decoder_weights2,
        'decoder_bias2': decoder_bias2,
        'decoder_weights3': decoder_weights3,
        'decoder_bias3': decoder_bias3,
        'm_encoder_weights0': m_encoder_weights0,
        'v_encoder_weights0': v_encoder_weights0,
        'm_encoder_bias0': m_encoder_bias0,
        'v_encoder_bias0': v_encoder_bias0,
        'm_encoder_weights1': m_encoder_weights1,
        'v_encoder_weights1': v_encoder_weights1,
        'm_encoder_bias1': m_encoder_bias1,
        'v_encoder_bias1': v_encoder_bias1,
        'm_encoder_weights2': m_encoder_weights2,
        'v_encoder_weights2': v_encoder_weights2,
        'm_encoder_bias2': m_encoder_bias2,
        'v_encoder_bias2': v_encoder_bias2,
        'm_decoder_weights1': m_decoder_weights1,
        'v_decoder_weights1': v_decoder_weights1,
        'm_decoder_bias1': m_decoder_bias1,
        'v_decoder_bias1': v_decoder_bias1,
        'm_decoder_weights2': m_decoder_weights2,
        'v_decoder_weights2': v_decoder_weights2,
        'm_decoder_bias2': m_decoder_bias2,
        'v_decoder_bias2': v_decoder_bias2,
        'm_decoder_weights3': m_decoder_weights3,
        'v_decoder_weights3': v_decoder_weights3,
        'm_decoder_bias3': m_decoder_bias3,
        'v_decoder_bias3': v_decoder_bias3
    }
    # Save the trained model along with training set
    save_model(model, x_train, x_val, 'autoencoder_model.pkl')

    # Compress and decompress data
    selected_file = 'test'
    with open(selected_file, 'rb') as f:
        binary_data = f.read()

    bit_array = binary_to_bit_array(binary_data)
    data_chunks = chunk_data(bit_array, chunk_size)

    reconstructed_data = []
    original_lengths = []

    for i, chunk in enumerate(data_chunks):
        chunk = np.array(list(chunk), dtype=np.uint8)
        chunk = np.expand_dims(chunk, axis=0)
        encoder_output_val1 = sigmoid(np.dot(chunk, encoder_weights1) + encoder_bias1)
        encoded_val = sigmoid(np.dot(encoder_output_val1, encoder_weights2) + encoder_bias2)

        compressed_chunk = encoded_val
        decoder_output_val1 = sigmoid(np.dot(compressed_chunk, decoder_weights1) + decoder_bias1)
        decoded_val = sigmoid(np.dot(decoder_output_val1, decoder_weights2) + decoder_bias2)

        reconstructed_chunk = decoded_val
        print(f"{i}/{len(data_chunks)}")

        reconstructed_chunk = remove_padding(reconstructed_chunk.squeeze(), [8])
        reconstructed_data.append(reconstructed_chunk)
        original_lengths.append(len(chunk[0]))

    compressed_data = np.array(reconstructed_data)
    compressed_data_uint8 = compressed_data.astype(np.float64)

    compressed_data_bytes = compressed_data_uint8.tobytes()

    with open(f'{selected_file}.AIZip', 'wb') as file:
        file.write(compressed_data_bytes)

    selected_file = f'{selected_file}.AIZip'

    if selected_file and selected_file.endswith('.AIZip'):
        with open(selected_file, 'rb') as file:
            compressed_data_bytes = file.read()

        compressed_data_uint8 = np.frombuffer(compressed_data_bytes, dtype=np.float64)

        encoding_dim = 4

        num_chunks = len(compressed_data_uint8) // encoding_dim
        compressed_data = compressed_data_uint8[:num_chunks * encoding_dim].reshape((num_chunks, encoding_dim))

        original_data = []
        reconstructed_data = []

        for i, chunk in enumerate(compressed_data):
            chunk = np.expand_dims(chunk, axis=0)
            decoder_output_val1 = sigmoid(np.dot(chunk, decoder_weights1) + decoder_bias1)
            decoded_val = sigmoid(np.dot(decoder_output_val1, decoder_weights2) + decoder_bias2)

            reconstructed_chunk = decoded_val
            print(f"{i}/{len(compressed_data)}")

            reconstructed_chunk = remove_padding(reconstructed_chunk.squeeze(), [8])

            reconstructed_data.append(reconstructed_chunk)

        reconstructed_data = np.round(reconstructed_data, 0)
        reconstructed_data = reconstructed_data.astype(np.uint8)

        reconstructed_data = [''.join(map(str, map(int, b))) for b in reconstructed_data]
        reconstructed_data_bit_chunks = [chunk_string(b, 8) for b in reconstructed_data]

        byte_array = bytearray([int(b, 2) for sublist in reconstructed_data_bit_chunks for b in sublist])

        with open(selected_file[:-6], 'wb') as file:
            file.write(byte_array)

if __name__ == "__main__":
    main()
