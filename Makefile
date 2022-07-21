
build:
	python3 setup.py sdist bdist_wheel

clean:
	python3 setup.py clean
	rm -rf dist

publish:
	twine check dist/*
	twine upload dist/*

.PHONY: build clean publish
