FROM python:3.8-slim-buster

<<<<<<< HEAD
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
=======
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app.py /app

CMD ["python", "app.py"]
>>>>>>> d9a92ad3d26ce276ce68b0db9bf5258e4dcfe726
