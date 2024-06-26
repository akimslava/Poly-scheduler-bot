FROM python:3.9

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV PYTHONPATH=/app:$PYTHONPATH

WORKDIR /app

CMD ["python", "src/main.py"]
