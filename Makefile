run:
	python -m doob_bot

test:
	pip install -r requirements.txt
	sh run-tests.sh

build:
	docker build --build-arg token=${BOT_TOKEN} -t doob_bot .
