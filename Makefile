# Makefile para el Proyecto de Clasificación de Vinos

# Variables
PYTHON = python3
PIP = pip
STREAMLIT = streamlit
UVICORN = uvicorn
DOCKER = docker
APP_NAME = wine-classifier
PORT = 80

# Comandos de Python
install:
	pip install -r requirements.txt

run-visual:
	python3 wine_dataset_script.py

run-streamlit:
	streamlit run streamlit_wine_app.py

run-api:
	uvicorn fastapi_wine_api:app --reload

# Comandos de Docker
docker-build:
	docker build -t $(APP_NAME) .

docker-run:
	docker run -d -p 80:$(PORT)80 $(APP_NAME)

docker-stop:
	docker stop $$(docker ps -q --filter ancestor=$(APP_NAME))

docker-clean: docker-stop
	docker rm $$(docker ps -a -q --filter ancestor=$(APP_NAME))
	docker rmi $(APP_NAME)

# Comandos de limpieza
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

# Comando para ejecutar tests (asumiendo que tienes tests)
test:
	python3 -m pytest tests/

# Comando para verificar el estilo del código
lint:
	flake8 .

# Comando para formatear el código
format:
	black .

# Comando para generar documentación (asumiendo que usas Sphinx)
docs:
	cd docs && make html

run: run-visual run-streamlit run-api

.PHONY: install run-visualization run-streamlit run-api docker-build docker-run docker-stop docker-clean clean test lint format docs
