# API Калькулятор

Высокопроизводительный API для выполнения базовых математических операций на FastAPI.

## Запуск в Docker

1. Собрать образ:
   docker build -t calc-api:1.0.0 .
2. Запустить контейнер:
   docker run -d --name calc-api -p 8000:8000 calc-api:1.0.0

## Документация API

http://localhost:8000/docs

## Поддерживаемые операции

- add — сложение
- subtract — вычитание
- multiply — умножение
- divide — деление