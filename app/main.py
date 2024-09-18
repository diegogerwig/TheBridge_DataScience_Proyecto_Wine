from fastapi import FastAPI
from pydantic import BaseModel, confloat, conint

app = FastAPI()

# Definición del modelo con validaciones
class WineFeatures(BaseModel):
    alcohol: confloat(ge=0) 
    malic_acid: confloat(ge=0)
    ash: confloat(ge=0)
    alcalinity_of_ash: confloat(ge=0)
    magnesium: conint(ge=0)  # entero mayor que 0
    total_phenols: confloat(ge=0)
    flavanoids: confloat(ge=0)
    nonflavanoid_phenols: confloat(ge=0)
    proanthocyanins: confloat(ge=0)
    color_intensity: confloat(ge=0)
    hue: confloat(ge=0)
    od280_od315_of_diluted_wines: confloat(ge=0)
    proline: conint(ge=0)


@app.post("/predict")
def predict(wine_features: WineFeatures):
    # Aquí se debe realizar la lógica de predicción
    return {
        "predicted_class": "Clase 1",
        "probabilities": {"Clase 1": 0.8, "Clase 2": 0.1, "Clase 3": 0.1}
    }


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de clasificación de Vinos"}