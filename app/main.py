# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine
import os

app = FastAPI()

current_dir = os.path.dirname(os.path.realpath(__file__))

# Cargar el modelo entrenado
model_path = os.path.join(current_dir, '../model', 'model.pkl')
model = joblib.load(model_path)

# Intentar cargar el scaler, si no existe, crear uno nuevo
scaler_path = os.path.join(current_dir, 'model', 'scaler.pkl')

# Cargar el scaler (asumiendo que lo guardaste
try:
    scaler = joblib.load('./model/scaler.pkl')
except FileNotFoundError:
    # Si el scaler no existe, creamos uno nuevo y lo ajustamos con los datos originales
    wine = load_wine()
    X = wine.data
    scaler = StandardScaler()
    scaler.fit(X)
    # Guardar el scaler para futuros usos
    joblib.dump(scaler, './model/scaler.pkl')

class WineFeatures(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float

@app.post("/predict")
async def predict_wine(features: WineFeatures):
    # Convertir las características a un array numpy
    input_data = np.array([[
        features.alcohol, features.malic_acid, features.ash,
        features.alcalinity_of_ash, features.magnesium,
        features.total_phenols, features.flavanoids,
        features.nonflavanoid_phenols, features.proanthocyanins,
        features.color_intensity, features.hue,
        features.od280_od315_of_diluted_wines, features.proline
    ]])
    
    # Escalar los datos de entrada
    input_data_scaled = scaler.transform(input_data)
    
    # Hacer la predicción
    prediction = model.predict(input_data_scaled)
    probabilities = model.predict_proba(input_data_scaled)[0]
    
    wine_class_names = {
        0: "VINO TINTO",
        1: "VINO ROSADO",
        2: "VINO BLANCO"
    }
    
    predicted_wine = wine_class_names[prediction[0]]
    
    return {
        "predicted_class": predicted_wine,
        "probabilities": {
            "VINO TINTO": probabilities[0],
            "VINO ROSADO": probabilities[1],
            "VINO BLANCO": probabilities[2]
        }
    }

@app.get("/")
async def root():
    return {"message": "Bienvenido al clasificador de vinos API de DIEGO GERWIG"}
