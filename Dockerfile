FROM python:3.10.4


COPY ./ /app
WORKDIR /app

# RUN python3 -m pip install -U python-dotenv
RUN pip install python-dotenv
RUN python3 -m pip install -U discord.py

CMD python3 bot.py
