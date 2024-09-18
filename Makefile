APP_NAME = wine-classifier


req:
	pip install -r requirements.txt

run-visual:
	python3 ./src/wine_dataset_script.py

run-streamlit:
	streamlit run ./src/streamlit_wine_app.py

run-api:
	uvicorn fastapi_wine_api:app --reload

docker-build:
	docker build -t $(APP_NAME) .

docker-run:
	docker run -d -p 80:80 $(APP_NAME)

docker-stop:
	docker stop $$(docker ps -q --filter ancestor=$(APP_NAME))

docker-clean: docker-stop
	docker rm $$(docker ps -a -q --filter ancestor=$(APP_NAME))
	docker rmi $(APP_NAME)

clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

test:
	python3 -m pytest tests/

lint:
	flake8 .

format:
	black .

docs:
	cd docs && make html

run: run-visual run-streamlit run-api

.PHONY: req run-visual run-streamlit run-api docker-build docker-run docker-stop docker-clean clean test lint format docs run