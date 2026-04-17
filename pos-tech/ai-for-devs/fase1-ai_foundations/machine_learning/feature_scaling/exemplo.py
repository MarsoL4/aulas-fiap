# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Criando um conjunto de dados fictício de previsão de crédito
np.random.seed(42)

# Gerando dados aleatórios
n_samples = 1000
idade = np.random.randint(18, 65, size=n_samples)
salario = np.random.randint(20000, 150000, size=n_samples)
historico_credito = np.random.choice(['bom', 'ruim'], size=n_samples)
score = np.random.randint(300, 850, size=n_samples)
numero_emprestimos = np.random.randint(0, 5, size=n_samples)

# Criando a variável alvo (1 para aprovado, 0 para não aprovado)
alvo = np.where((idade < 30) & (salario > 70000) & (historico_credito == 'bom'), 1, 0)

# Criando o DataFrame
data = pd.DataFrame({
    'idade': idade,
    'salario': salario,
    'historico_credito': historico_credito,
    'score': score,
    'numero_emprestimos': numero_emprestimos,
    'alvo': alvo
})

# Usando LabelEncoder para transformar variáveis categóricas em numéricas 
label_encoder = LabelEncoder()
data['historico_credito'] = label_encoder.fit_transform(data['historico_credito'])

# Embaralhando o conjunto de dados
data_shuffled = data.sample(frac=1, random_state=42)

# Salvando o conjunto de dados embaralhado em um arquivo CSV
data_shuffled.to_csv('dataset_credito_embaralhado_com_features.csv', index=False)

# Carregando o conjunto de dados fictício de previsão de crédito
data = data_shuffled

# Pré-processamento dos dados
# Vamos supor que o conjunto de dados possui as seguintes colunas: 'idade', 'salario', 'historico_credito', 'alvo' (0 para não aprovado, 1 para aprovado)

# Separando features (X) e target (y)
X = data.drop('alvo', axis=1)
y = data['alvo']

# Dividindo o conjunto de dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
# Inicializar o scaler usando apenas o conjunto de treino
scaler = StandardScaler()
scaler.fit(X_train)
# Aplicar o Z-score nas features de treino
X_train_scaled = scaler.transform(X_train)
# Aplicar o Z-score nas features de teste usando as estatísticas do conjunto de treino
X_test_scaled = scaler.transform(X_test)