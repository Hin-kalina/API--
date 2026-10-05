from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Инициализация приложения FastAPI
app = FastAPI(
    title="API Калькулятор",
    description="Высокопроизводительный API для выполнения базовых математических операций",
    version="1.0.0"
)

# Модель данных для входящего запроса (обеспечивает валидацию)
class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str  # Допустимые значения: add, subtract, multiply, divide

@app.post("/calculate", tags=["Вычисления"])
async def calculate(request: CalculationRequest):
    """
    Эндпоинт для выполнения математических операций.
    Принимает два числа и строку с названием операции.
    """
    a, b, op = request.a, request.b, request.operation

    if op == "add":
        result = a + b
    elif op == "subtract":
        result = a - b
    elif op == "multiply":
        result = a * b
    elif op == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Ошибка: деление на ноль!")
        result = a / b
    else:
        raise HTTPException(status_code=400, detail="Неподдерживаемая операция. Используйте: add, subtract, multiply, divide")

    return {"operation": op, "operand_a": a, "operand_b": b, "result": result}

@app.get("/", tags=["Служебное"])
async def root():
    return {"message": "Добро пожаловать в API Калькулятор. Документация доступна по адресу /docs"}

