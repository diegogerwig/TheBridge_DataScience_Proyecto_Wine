APP_NAME = wine_classifier


req:
	pip install -r requirements.txt

run-visual:
	python3 ./src/wine_dataset_script.py

run-streamlit:
	streamlit run ./src/streamlit_wine_app.py

run-api:
	uvicorn app.main:app --reload

test-api:
	python3 -m pytest ./app/tests/test.py --disable-warnings

run: run-visual run-streamlit run-api

.PHONY: req run-visual run-streamlit run-api test-api clean test run