FROM python:3.7

ARG token
WORKDIR /opt

COPY . .

RUN pip install -r requirements.txt && \
    pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip#egg=discord.py && \
    pip install .

ENV BOT_TOKEN=$token
ENV SPY_LOG_LOGGER="pretty-no-meta"

CMD ["python", "./doob_bot/__init__.py"]
