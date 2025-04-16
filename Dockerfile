FROM python:3.10-slim-buster
WORKDIR /app
COPY ./app /app

RUN apt update -y && apt install awscli -y

RUN apt-get update && apt pip install -r requirements.txt
CMD ["python3", "app.py"]