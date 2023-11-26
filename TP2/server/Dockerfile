FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 32211

CMD python app.py --host=0.0.0.0 --port 32211