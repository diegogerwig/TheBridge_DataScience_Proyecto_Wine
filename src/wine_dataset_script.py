import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target

df.to_csv('./data/wine_dataset.csv', index=False)

print(df.head())

plt.figure(figsize=(12, 10))
df.hist(figsize=(12, 10), bins=20)
plt.tight_layout()
plt.title('Histogramas de las Características del Vino')
plt.savefig('./plots/histograms_wine_dataset.png')
print('✅ Plot saved as histograms_wine_dataset.png')

plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Matriz de Correlación de las Características del Vino')
plt.savefig('./plots/correlation_matrix_wine_dataset.png')
print('✅ Plot saved as correlation_matrix_wine_dataset.png')

print(df.describe())
