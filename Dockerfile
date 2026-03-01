FROM python:3.9-slim
WORKDIR /app


ENV PYTHONUNBUFFERED=1

RUN pip install requests
COPY monitor.py .
CMD ["python", "monitor.py"]
