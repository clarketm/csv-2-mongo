.PHONY: format
format:
	python -m black .

.PHONY: build
build: clean
	rm -rf ./dist/*
	python3 setup.py sdist bdist_wheel

.PHONY: test
test:
	@echo "not implemented"

.PHONY: clean
clean:
	rm -rf ./dist ./build ./*.egg-info ./htmlcov
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: binary make
binary make:
	pyinstaller --hidden-import='pandas._libs.tslibs.timedeltas' --onefile ./csv_2_mongo.py

.PHONY: check
check:
	twine check dist/*

.PHONY: upload-test
upload-test: test clean build check
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

.PHONY: upload
upload: test clean build check
	twine upload dist/*

