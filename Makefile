
install:
	python setup.py develop

publish:
	poetry build
	poetry publish