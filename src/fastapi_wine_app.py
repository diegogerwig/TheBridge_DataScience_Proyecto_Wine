from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_wine
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

app = FastAPI()

# Cargar el dataset de Vinos y entrenar el modelo
wine = load_wine()
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

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
def predict(features: WineFeatures):
    # Realizar predicción
    prediction = model.predict([[
        features.alcohol,
        features.malic_acid,
        features.ash,
        features.alcalinity_of_ash,
        features.magnesium,
        features.total_phenols,
        features.flavanoids,
        features.nonflavanoid_phenols,
        features.proanthocyanins,
        features.color_intensity,
        features.hue,
        features.od280_od315_of_diluted_wines,
        features.proline
    ]])
    return {"wine_class": wine.target_names[prediction[0]]}

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de clasificación de Vinos"}
