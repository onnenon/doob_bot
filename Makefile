run:
	python doob_bot/main.py

test:
	python -m coverage run --source doob_bot -m pytest tests -p no:warnings
	python -m coverage report

build:
	docker build --build-arg token=${BOT_TOKEN} -t doob_bot .

format:
	black doob_bot tests
	isort doob_bot tests


