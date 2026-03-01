# 1. Базовый образ с Python
FROM python:3.9-slim

# 2. Рабочая директория
WORKDIR /app

# 3. Устанавливаем библиотеку для запросов (это команда RUN)
RUN pip install requests

# 4. Копируем наш код
COPY monitor.py .

# 5. Запускаем
CMD ["python", "monitor.py"]
