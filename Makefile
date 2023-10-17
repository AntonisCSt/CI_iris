VENV_PATH = "venv/Scripts/activate"

default:
	echo "Hello"

test: train
	pytest .

quality_check:
	isort ./
	black ./
	find . -type f -name "*.py" | xargs pylint --recursive=yes .

load_data:
	python load_iris_data.py
	@echo "finished loading"
	echo "last message of load_data"

train: load_data
	python ml_pipeline_training_example.py

venv:
	python -m venv venv

activate_venv: venv
	@echo "Activating virtual environment..."
	@source ${VENV_PATH}

install: activate_venv
	venv/Scripts/pip install -r requirements.txt

build: install
	@echo "Build completed"

