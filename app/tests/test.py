import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Test que verifica el mensaje de bienvenida correcto
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido a la API de clasificación de Vinos"}

# Test que verifica que la predicción funcione correctamente
def test_predict():
    wine_features = {
        "alcohol": 14.23,
        "malic_acid": 1.71,
        "ash": 2.43,
        "alcalinity_of_ash": 15.6,
        "magnesium": 127,
        "total_phenols": 2.8,
        "flavanoids": 3.06,
        "nonflavanoid_phenols": 0.28,
        "proanthocyanins": 2.29,
        "color_intensity": 5.64,
        "hue": 1.04,
        "od280_od315_of_diluted_wines": 3.92,
        "proline": 1065
    }
    response = client.post("/predict", json=wine_features)
    assert response.status_code == 200
    result = response.json()
    assert "predicted_class" in result
    assert "probabilities" in result
    assert isinstance(result["predicted_class"], str)
    assert isinstance(result["probabilities"], dict)

# Test que verifica la respuesta ante campos faltantes
def test_predict_missing_fields():
    wine_features_incomplete = {
        "alcohol": 14.23,
        "malic_acid": 1.71,
        "ash": 2.43,
        "magnesium": 127,
        "total_phenols": 2.8
        # Falta el resto de las características
    }
    response = client.post("/predict", json=wine_features_incomplete)
    assert response.status_code == 422  # La API debe devolver un error 422
    assert "detail" in response.json()

# Test que verifica la respuesta ante tipos de datos incorrectos
def test_predict_invalid_data_type():
    wine_features_invalid = {
        "alcohol": "14.23",  # String en vez de float
        "malic_acid": 1.71,
        "ash": 2.43,
        "alcalinity_of_ash": 15.6,
        "magnesium": 127,
        "total_phenols": 2.8,
        "flavanoids": 3.06,
        "nonflavanoid_phenols": 0.28,
        "proanthocyanins": 2.29,
        "color_intensity": 5.64,
        "hue": 1.04,
        "od280_od315_of_diluted_wines": 3.92,
        "proline": 1065
    }
    response = client.post("/predict", json=wine_features_invalid)
    assert response.status_code == 422  # La API debe devolver un error 422 por tipo incorrecto
    assert "detail" in response.json()

# Test que verifica valores fuera de rango
def test_predict_out_of_range():
    wine_features_out_of_range = {
        "alcohol": -5.0,  # Valor inválido fuera de rango
        "malic_acid": 1.71,
        "ash": 2.43,
        "alcalinity_of_ash": 15.6,
        "magnesium": 127,
        "total_phenols": 2.8,
        "flavanoids": 3.06,
        "nonflavanoid_phenols": 0.28,
        "proanthocyanins": 2.29,
        "color_intensity": 5.64,
        "hue": 1.04,
        "od280_od315_of_diluted_wines": 3.92,
        "proline": 1065
    }
    response = client.post("/predict", json=wine_features_out_of_range)
    assert response.status_code == 422  # La API debe devolver un error 422 por valores fuera de rango
    assert "detail" in response.json()

# Test que verifica la solicitud vacía
def test_predict_empty_request():
    response = client.post("/predict", json={})
    assert response.status_code == 422  # La API debe devolver un error 422 por solicitud vacía
    assert "detail" in response.json()
