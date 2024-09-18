import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Cargar el dataset de Vinos
wine = load_wine()
X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar un modelo simple
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

st.title('Clasificador de Vinos')

# Crear sliders para las características
feature_input = {}
for feature in wine.feature_names:
    feature_input[feature] = st.slider(
        f'{feature}',
        float(X[feature].min()),
        float(X[feature].max()),
        float(X[feature].mean())
    )

# Botón para realizar la predicción
if st.button('Clasificar Vino'):
    input_data = np.array(list(feature_input.values())).reshape(1, -1)
    prediction = model.predict(input_data)
    st.write(f'El vino clasificado pertenece a la clase: {wine.target_names[prediction[0]]}')

# Mostrar importancia de características
st.subheader('Importancia de las Características')
feature_importance = pd.DataFrame({
    'feature': wine.feature_names,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

st.bar_chart(feature_importance.set_index('feature'))

# Mostrar datos
st.subheader('Muestra del Dataset de Vinos:')
st.write(X.head())
