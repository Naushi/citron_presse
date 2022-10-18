compile-requirements:
	pip-compile requirements.in

lint:
	isort app/ --check
	black app/ --check
	mypy app/

format:
	isort app/
	black app/