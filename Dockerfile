FROM python:3.10-slim-buster

WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y
RUN apt-get update && pip install -r requirements.txt

# Expose the port your app will run on
EXPOSE 8080

# Run the FastAPI app via uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
