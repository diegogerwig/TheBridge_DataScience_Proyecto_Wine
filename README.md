# TheBridge_DataScience_Proyecto_Wine

Este proyecto implementa un clasificador de vinos utilizando el dataset de Vinos de scikit-learn. Incluye scripts para visualización de datos, una aplicación web interactiva con Streamlit y una API REST con FastAPI.

## Contenido del Proyecto

1. Script de visualización de datos
2. Aplicación web Streamlit
3. API REST con FastAPI
4. Dockerfile para contenerización

## Requisitos

- Python 3.7+
- pip
- Docker (opcional, para contenerización)

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/tu-usuario/clasificador-vinos.git
   cd clasificador-vinos
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Uso

### Script de Visualización

Para ejecutar el script de visualización:

```
python visualize_wine_data.py
```

Este script cargará el dataset de Vinos, mostrará algunas estadísticas básicas y generará visualizaciones.

### Aplicación Streamlit

Para ejecutar la aplicación web Streamlit:

```
streamlit run streamlit_wine_app.py
```

Esto iniciará un servidor local y abrirá la aplicación en tu navegador predeterminado.

### API FastAPI

Para ejecutar la API:

```
uvicorn fastapi_wine_api:app --reload
```

La API estará disponible en `http://localhost:8000`. Puedes acceder a la documentación interactiva en `http://localhost:8000/docs`.

## Contenerización

Para construir y ejecutar el contenedor Docker:

```
docker build -t wine-classifier .
docker run -d -p 80:80 wine-classifier
```

La API estará disponible en `http://localhost`.

## Estructura del Proyecto

```
clasificador-vinos/
│
├── visualize_wine_data.py
├── streamlit_wine_app.py
├── fastapi_wine_api.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de crear un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.
