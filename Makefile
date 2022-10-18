compile-requirements:
	pip-compile requirements.in

lint:
	black .