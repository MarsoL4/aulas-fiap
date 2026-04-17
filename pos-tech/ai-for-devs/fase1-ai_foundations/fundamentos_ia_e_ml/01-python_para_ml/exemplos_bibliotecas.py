# Exemplo de uso da biblioteca NumPy para calcular a média de um array
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mean = np.mean(data)
print(mean)
#-------------------------------------------------------------------------------------------#

# Exemplo de uso da biblioteca Scipy para resolver uma equação diferencial
from scipy.integrate import solve_ivp

def dydt(t, y):
   return -0.5 * y
solution = solve_ivp(dydt, [0, 10], [2])
print(solution.y)
#-------------------------------------------------------------------------------------------#

# Exemplo de uso da biblioteca Pandas para ler um arquivo CSV e calcular a média de uma coluna
import pandas as pd
data = pd.read_csv('data.csv')
mean_value = data['column_name'].mean()
print(mean_value)
#-------------------------------------------------------------------------------------------#

#Exemplo de uso da biblioteca Matplotlib para criar um gráfico simples
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.show()
#-------------------------------------------------------------------------------------------#

# Exemplo de uso da biblioteca Seaborn para criar um gráfico de distribuição
import seaborn as sns

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
sns.histplot(data)
plt.show()
#-------------------------------------------------------------------------------------------#

# Exemplo de uso da biblioteca Scikit-learn para treinar um modelo de regressão linear
from sklearn.linear_model import LinearRegression

X = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
y = np.dot(X, np.array([1, 2])) + 3

model = LinearRegression().fit(X, y)
print(model.coef_)
#-------------------------------------------------------------------------------------------#

# Exemplo de uso da biblioteca TensorFlow para criar e treinar um modelo de rede neural
import tensorflow as tf

# Exemplo de dados de entrada
# X: matriz com 100 amostras e 3 características
# y: vetor de saída com 100 valores
X = np.random.random((100, 3))
y = np.random.random((100, 1))

# Definindo o modelo usando Input
inputs = tf.keras.Input(shape=(3,))
x = tf.keras.layers.Dense(10, activation='relu')(inputs)
outputs = tf.keras.layers.Dense(1)(x)
model = tf.keras.Model(inputs=inputs, outputs=outputs)

# Compilando o modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Treinando o modelo
model.fit(X, y, epochs=5)
#-------------------------------------------------------------------------------------------#

# Exemplo de uso da biblioteca TensorFlow com Keras para criar e treinar um modelo de rede neural usando Sequential

# Exemplo de dados de entrada
# X: matriz com 100 amostras e 8 características
# y: vetor de saída com 100 valores binários (0 ou 1)
X = np.random.random((100, 8))
y = np.random.randint(2, size=(100, 1))

# Definindo o modelo com *Keras*
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(12, input_dim=8, activation='relu'))
model.add(tf.keras.layers.Dense(8, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

# Compilando o modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinando o modelo
model.fit(X, y, epochs=150, batch_size=10)
#-------------------------------------------------------------------------------------------#

# Exemplo de uso da biblioteca PyTorch para criar e treinar um modelo de rede neural
import torch
import torch.nn as nn
import torch.optim as optim

# Exemplo de dados de entrada
# X: matriz com 100 amostras e 3 características
# y: vetor de saída com 100 valores
X = torch.randn(100, 3)  # Gera uma matriz de 100x3 com valores aleatórios
y = torch.randn(100, 1)  # Gera um vetor de 100x1 com valores aleatórios

class SimpleNN(nn.Module):
   def __init__(self):
       super(SimpleNN, self).__init__()
       self.fc1 = nn.Linear(3, 10)
       self.fc2 = nn.Linear(10, 1)

   def forward(self, x):
       x = torch.relu(self.fc1(x))
       x = self.fc2(x)
       return x

model = SimpleNN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(100):
   optimizer.zero_grad()
   outputs = model(X)
   loss = criterion(outputs, y)
   loss.backward()
   optimizer.step()
   print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')