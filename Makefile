.PHONY: setup

env:
	pyvenv env
	./env/bin/pip install -r requirements.txt
	./env/bin/pip install .


setup: env


lint: env
	./env/bin/flake8 ika_mining
