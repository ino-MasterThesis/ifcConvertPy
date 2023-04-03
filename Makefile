lint:
	-pipenv shell
	flake8 ./src
	isort --check --diff ./src
	black --check ./src

format:
	-pipenv shell
	isort ./src
	black ./src
