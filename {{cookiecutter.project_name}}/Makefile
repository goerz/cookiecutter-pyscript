TESTPYPI = https://testpypi.python.org/pypi

install:
	pip install .

develop:
	pip install -e .[dev]

uninstall:
	pip uninstall {{cookiecutter.module_name }}

upload:
	python setup.py register
	python setup.py sdist upload

test-upload:
	python setup.py register -r $(TESTPYPI)
	python setup.py sdist upload -r $(TESTPYPI)

test-install:
	pip install -i $(TESTPYPI) {{cookiecutter.project_name }}

.PHONY: install develop uninstall upload test-upload test-install
