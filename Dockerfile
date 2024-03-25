FROM python:3.10-slim

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./main.py ./

VOLUME /app/config.py

CMD ["python","main.py"]
