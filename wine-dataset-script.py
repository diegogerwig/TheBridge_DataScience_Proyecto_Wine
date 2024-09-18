import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

# Cargar el dataset de Vinos
wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target

# Mostrar las primeras filas del dataset
print(df.head())

# Visualizar la distribución de las características
plt.figure(figsize=(12, 10))
df.hist(figsize=(12, 10), bins=20)
plt.tight_layout()
plt.show()

# Matriz de correlación
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación de las Características del Vino')
plt.show()

# Estadísticas básicas
print(df.describe())
