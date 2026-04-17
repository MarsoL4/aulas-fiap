import torch
import torch.nn as nn
import torch.optim as optim

# --- 1. PREPARAÇÃO DOS DADOS ---
# X representa as entradas (distância) e y os alvos (tempo de conclusão)
# O .float32 é importante para garantir compatibilidade com os pesos da rede
X = torch.tensor([[5.0], [10.0], [10.0], [5.0], [10.0],
                  [5.0], [10.0], [10.0], [5.0], [10.0],
                  [5.0], [10.0], [10.0], [5.0], [10.0],
                  [5.0], [10.0], [10.0], [5.0], [10.0]], dtype=torch.float32)

y = torch.tensor([[30.5], [63.0], [67.0], [29.0], [62.0],
                  [30.5], [63.0], [67.0], [29.0], [62.0],
                  [30.5], [63.0], [67.0], [29.0], [62.0],
                  [30.5], [63.0], [67.0], [29.0], [62.0]], dtype=torch.float32)

# --- 2. DEFINIÇÃO DA ARQUITETURA DA REDE ---
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Camada densa 1: recebe 1 valor de entrada e gera 5 saídas
        self.fc1 = nn.Linear(1, 5) 
        # Camada densa 2: recebe as 5 saídas anteriores e gera 1 valor final (o tempo)
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        # Passa os dados pela primeira camada e aplica a função de ativação ReLU (zera valores negativos)
        x = torch.relu(self.fc1(x))
        # Passa pelo última camada para obter o resultado final
        x = self.fc2(x)
        return x

# Instancia o modelo
model = Net()

# --- 3. CONFIGURAÇÃO DO TREINAMENTO ---
# Função de perda: Mede o erro entre a previsão e o valor real (Mean Squared Error)
criterion = nn.MSELoss()
# Otimizador: Algoritmo que ajusta os pesos para diminuir o erro (SGD = Stochastic Gradient Descent)
# lr=0.01 é a taxa de aprendizado (quão grandes são os passos do ajuste)
optimizer = optim.SGD(model.parameters(), lr=0.01)

# --- 4. LOOP DE TREINAMENTO ---
for epoch in range(1000):
    # Limpa os gradientes acumulados da rodada anterior
    optimizer.zero_grad()
    
    # Forward: O modelo tenta prever os resultados com base em X
    outputs = model(X)
    
    # Calcula o erro (distância entre o que o modelo previu e o valor real y)
    loss = criterion(outputs, y)
    
    # Backward: Calcula o quanto cada peso da rede contribuiu para o erro
    loss.backward()
    
    # Atualiza os pesos de fato usando os cálculos do backward
    optimizer.step()
    
    # Mostra o progresso a cada 100 épocas
    if epoch % 100 == 99:
        print(f'Epoch {epoch+1}, Loss: {loss.item()}')

# --- 5. PREVISÃO ---
# torch.no_grad() desativa o cálculo de gradientes, economizando memória na hora de testar
with torch.no_grad():
    # Testando o modelo com uma distância de 10.0
    distancia_teste = torch.tensor([[10.0]], dtype=torch.float32)
    predicted = model(distancia_teste)
    
    # .item() transforma o tensor do PyTorch em um número comum do Python
    print(f'Previsão de tempo de conclusão: {predicted.item():.2f} minutos')