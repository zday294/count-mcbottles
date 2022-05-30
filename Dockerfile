FROM python:3.10

COPY ./ /app
WORKDIR /app

RUN pip3 install -U python-dotenv
RUN pip3 install discord.py

CMD python3 bot.py