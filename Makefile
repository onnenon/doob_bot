run:
	python3 __init__.py

test:
	pip install -r requirements.txt
	python -m unittest discover
