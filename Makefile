# Define the command to activate the virtual environment
ACTIVATE_VENV := . $(shell pwd)/venv/bin/activate

install:
	@$(ACTIVATE_VENV) && pip install -r requirements.txt