FROM python:3.12.0b1-alpine3.18

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]