import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

wine = load_wine()

X = pd.DataFrame(wine.data, columns=wine.feature_names)
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

joblib.dump(model, './model/model.pkl')
print('✅ Model saved as model.pkl')

y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)

st.title('Clasificador de Vinos')

st.write(f"Precisión del modelo en el conjunto de prueba: {accuracy:.2f}")

st.subheader("Reporte de Clasificación:")
st.text(classification_report(y_test, y_pred, target_names=wine.target_names))

# Sliders 
feature_input = {}
for feature in wine.feature_names:
    feature_input[feature] = st.slider(
        f'{feature}',
        float(X[feature].min()),
        float(X[feature].max()),
        float(X[feature].mean())
    )

if st.button('Clasificar Vino'):
    input_data = np.array(list(feature_input.values())).reshape(1, -1)
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)
    probabilities = model.predict_proba(input_data_scaled)[0]
    
    st.write(f'El vino clasificado pertenece a la clase: {wine.target_names[prediction[0]]}')
    
    st.subheader("Probabilidades de cada clase:")
    for class_name, prob in zip(wine.target_names, probabilities):
        st.write(f"{class_name}: {prob:.4f}")

st.subheader('Importancia de las Características')
feature_importance = pd.DataFrame({
    'feature': wine.feature_names,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

st.bar_chart(feature_importance.set_index('feature'))

st.subheader('Muestra del Dataset de Vinos:')
st.write(X.head())

st.subheader('Distribución de Clases en el Dataset')
class_distribution = pd.Series(y).value_counts().sort_index()
st.bar_chart(class_distribution)
