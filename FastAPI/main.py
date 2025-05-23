from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import asyncio
import time
import random

#uvicorn app:app --reload
app = FastAPI()

# Set up templates directory
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
os.makedirs(templates_dir, exist_ok=True)
templates = Jinja2Templates(directory=templates_dir)

# Set up static files directory
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})

@app.post("/calculate")
def calculate(data: dict):
    try:
        num1 = float(data.get("num1", 0))
        num2 = float(data.get("num2", 0))
        operation = data.get("operation", "add")
        
        result = 0
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return {"error": "Cannot divide by zero"}
            result = num1 / num2
            
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

@app.post("/async-calculate")
async def async_calculate(data: dict):
    """异步计算函数，模拟耗时计算过程"""
    try:
        num1 = float(data.get("num1", 0))
        num2 = float(data.get("num2", 0))
        operation = data.get("operation", "add")
        
        # 模拟耗时计算过程
        delay = random.uniform(1, 3)  # 随机延迟1-3秒
        await asyncio.sleep(delay)
        
        result = 0
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                return {"error": "Cannot divide by zero"}
            result = num1 / num2
        
        # 返回结果和计算耗时
        return {
            "result": result,
            "time_taken": f"{delay:.2f} seconds",
            "timestamp": time.time()
        }
    except Exception as e:
        return {"error": str(e)}