import numpy as np
import matplotlib.pyplot as plt

class DenseLayer:
    def __init__(self, input_size, output_size, activation_function):
        self.input_size = input_size
        self.output_size = output_size
        self.activation_function = activation_function
        self.weights = np.random.randn(output_size, input_size) * 0.01
        self.biases = np.zeros((output_size, 1))
        self.m_w = np.zeros_like(self.weights)
        self.v_w = np.zeros_like(self.weights)
        self.m_b = np.zeros_like(self.biases)
        self.v_b = np.zeros_like(self.biases)
        self.beta1 = 0.8
        self.beta2 = 0.999
        self.epsilon = 1e-8
        self.t = 0

    def forward(self, inputs):
        self.inputs = inputs
        self.z = np.dot(self.weights, inputs) + self.biases
        self.output = self.activation_function(self.z)
        return self.output

    def backward(self, gradient):
        gradient *= self.activation_function(self.z, derivative=True)
        # Clip gradients to prevent overflow
        gradient = np.clip(gradient, -1, 1)
        self.gradient_weights = np.dot(gradient, self.inputs.T)
        self.gradient_biases = np.sum(gradient, axis=1, keepdims=True)
        return np.dot(self.weights.T, gradient)

    def update(self, learning_rate):
        self.t += 1
        self.m_w = self.beta1 * self.m_w + (1 - self.beta1) * self.gradient_weights
        self.v_w = self.beta2 * self.v_w + (1 - self.beta2) * (self.gradient_weights ** 2)
        self.m_b = self.beta1 * self.m_b + (1 - self.beta1) * self.gradient_biases
        self.v_b = self.beta2 * self.v_b + (1 - self.beta2) * (self.gradient_biases ** 2)
        m_w_hat = self.m_w / (1 - self.beta1 ** self.t)
        v_w_hat = self.v_w / (1 - self.beta2 ** self.t)
        m_b_hat = self.m_b / (1 - self.beta1 ** self.t)
        v_b_hat = self.v_b / (1 - self.beta2 ** self.t)
        self.weights -= learning_rate * m_w_hat / (np.sqrt(v_w_hat) + self.epsilon)
        self.biases -= learning_rate * m_b_hat / (np.sqrt(v_b_hat) + self.epsilon)

class Autoencoder:
    def __init__(self, input_size, encoding_dim):
        self.input_size = input_size
        self.encoding_dim = encoding_dim
        self.encoder_layers = [
            DenseLayer(input_size, 128, self.sigmoid),
            DenseLayer(128, 64, self.sigmoid),
            DenseLayer(64, 32, self.sigmoid),
            DenseLayer(32, 16, self.sigmoid),
            DenseLayer(16, encoding_dim, self.sigmoid)
        ]
        self.decoder_layers = [
            DenseLayer(encoding_dim, 16, self.sigmoid),
            DenseLayer(16, 32, self.sigmoid),
            DenseLayer(32, 64, self.sigmoid),
            DenseLayer(64, 128, self.sigmoid),
            DenseLayer(128, input_size, self.sigmoid)
        ]

    def sigmoid(self, x, derivative=False):
        if derivative:
            return x * (1 - x)
        if x.all() >= 0:
            return 1 / (1 + np.exp(-x))
        else:
            exp_x = np.exp(x)
            return exp_x / (exp_x + 1)

    def forward(self, X, layers):
        output = X
        for layer in layers:
            output = layer.forward(output)
        return output

    def backward(self, gradient, layers):
        for layer in reversed(layers):
            gradient = layer.backward(gradient)
        return gradient

    def update(self, learning_rate):
        for layer in self.encoder_layers + self.decoder_layers:
            layer.update(learning_rate)

    def binary_cross_entropy_loss(self, X, decoded):
        epsilon = 1e-10
        loss = -np.mean(X * np.log(decoded + epsilon) + (1 - X) * np.log(1 - decoded + epsilon))
        return loss

    def train(self, X_train, X_val, epochs=100000, learning_rate=0.00001):
        train_losses = []
        val_losses = []
        epoch_losses = []  # Collect losses for every epoch
        for epoch in range(epochs):
            # Forward pass for encoder
            encoded = self.forward(X_train, self.encoder_layers)
            # Forward pass for decoder
            decoded = self.forward(encoded, self.decoder_layers)
            # Compute training loss
            train_loss = self.binary_cross_entropy_loss(X_train, decoded)
            train_losses.append(train_loss)
            # Compute validation loss
            encoded_val = self.forward(X_val, self.encoder_layers)
            decoded_val = self.forward(encoded_val, self.decoder_layers)
            val_loss = self.binary_cross_entropy_loss(X_val, decoded_val)
            val_losses.append(val_loss)
            print(train_loss, val_loss)
            # Backpropagation for decoder
            error = decoded - X_train
            gradient = error
            gradient = self.backward(gradient, self.decoder_layers)
            # Backpropagation for encoder
            _ = self.backward(gradient, self.encoder_layers)
            # Gradient descent
            self.update(learning_rate)
            epoch_losses.append(train_loss)  # Collect loss for this epoch
            if (epoch + 1) % 50 == 0:
                # Plot losses every 50 epochs
                plt.plot(epoch_losses, label=f'Epoch {epoch + 1}')
                epoch_losses = []  # Clear the list for next 50 epochs
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.title('Training Loss over Epochs')
        plt.legend()
        plt.show()
        return train_losses, val_losses

    def reconstruct(self, X):
        encoded = self.forward(X, self.encoder_layers)
        reconstructed = self.forward(encoded, self.decoder_layers)
        return reconstructed

# Example usage:
input_size = 8
encoding_dim = 4
autoencoder = Autoencoder(input_size, encoding_dim)

# Generate random binary training and validation data for testing
num_samples = 5120
X_train = np.random.randint(0, 2, size=(input_size, num_samples))
X_val = np.random.randint(0, 2, size=(input_size, num_samples))

# Train the autoencoder and collect losses
train_losses, val_losses = autoencoder.train(X_train, X_val)

# Test the autoencoder by reconstructing some data
X_test = X_train[:, :1]  # take a sample from X_train
reconstructed_data = autoencoder.reconstruct(X_test)

# Print the original and reconstructed data
print("Original Data:")
print(X_test)
print("\nReconstructed Data:")
print(np.round(reconstructed_data))
