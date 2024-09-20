import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Cargar el dataset de vinos
wine = load_wine()

X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target

# Dividir el dataset en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Entrenar el modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Guardar el modelo
joblib.dump(model, './model/model.pkl')
print('✅ Model saved as model.pkl')

# Hacer predicciones y calcular la precisión
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

# Configuración de la aplicación Streamlit
st.set_page_config(page_title="Clasificador de Vinos", page_icon="🍷")

# Sidebar con README
st.sidebar.subheader('README:')
st.sidebar.markdown('''
Este es un clasificador de vinos que utiliza un modelo de Random Forest. 
Puedes ajustar los valores de las características del vino en los sliders 
y el modelo te dirá a qué clase pertenece el vino.

Info del dataset: [Wine Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)

Info del proyecto: [GitHub](https://github.com/diegogerwig/TheBridge_DataScience_Proyecto_Wine/blob/main/README.md)

Streamlit: [Streamlit](https://wine-class-gerwig.streamlit.app/)
''', unsafe_allow_html=True)

# Contenido principal
st.title('Clasificador de Vinos')

st.write(f"Precisión del modelo en el conjunto de prueba: {accuracy:.2f}")

st.subheader("Reporte de Clasificación:")
st.text(classification_report(y_test, y_pred, target_names=wine.target_names))

# Sliders para las características del vino
feature_input = {}
for feature in wine.feature_names:
    feature_input[feature] = st.slider(
        f'{feature}',
        float(X[feature].min()),
        float(X[feature].max()),
        float(X[feature].mean())
    )

wine_class_names = {
    0: "VINO TINTO",
    1: "VINO ROSADO",
    2: "VINO BLANCO"
}

# Botón para clasificar el vino
if st.button('Clasificar Vino'):
    input_data = np.array(list(feature_input.values())).reshape(1, -1)
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)
    probabilities = model.predict_proba(input_data_scaled)[0]
    
    predicted_wine = wine_class_names[prediction[0]]
    st.write(f'El vino clasificado es: {predicted_wine}')
    
    st.subheader("Probabilidades de cada clase:")
    for i, (class_name, prob) in enumerate(zip(wine.target_names, probabilities)):
        st.write(f"{wine_class_names[i]}: {prob:.4f}")

# Importancia de las características
st.subheader('Importancia de las Características')
feature_importance = pd.DataFrame({
    'feature': wine.feature_names,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

st.bar_chart(feature_importance.set_index('feature'))

# Muestra del dataset
st.subheader('Muestra del Dataset de Vinos:')
st.write(X.head())

# Distribución de clases
st.subheader('Distribución de Clases en el Dataset')
class_distribution = pd.Series(y).value_counts().sort_index()
st.bar_chart(class_distribution)