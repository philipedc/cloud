FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

CMD ["./mv.sh"]

CMD ["echo $(ls ./rules)"]

CMD ["python", "rule_generator.py"]