
install:
	python setup.py develop

publish:
	poetry build
	poetry publish

test:
	pytest --cache-clear