from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import requests
import os
import json

# Initialize FastAPI app
app = FastAPI(title="Ollama Chat Web App")

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Ollama API base URL
OLLAMA_API_URL = "http://localhost:11434/api"


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # Get available models from Ollama
    try:
        models_response = requests.get(f"{OLLAMA_API_URL}/tags")
        models_data = models_response.json()
        models = [model["name"] for model in models_data["models"]]
    except Exception as e:
        models = []
        print(f"Error fetching models: {e}")
    
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "models": models}
    )


@app.post("/chat", response_class=HTMLResponse)
async def chat(
    request: Request,
    message: str = Form(...),
    model: str = Form(...),
):
    try:
        # Prepare the payload for Ollama API
        payload = {
            "model": model,
            "prompt": message,
            "stream": False
        }
        
        # Send request to Ollama API
        response = requests.post(f"{OLLAMA_API_URL}/generate", json=payload)
        data = response.json()
        
        # Extract the response text
        response_text = data.get("response", "No response from model")
        
    except Exception as e:
        response_text = f"Error: {str(e)}"
    
    return templates.TemplateResponse(
        "chat_response.html", 
        {"request": request, "message": message, "response": response_text}
    )


@app.get("/models")
async def get_models():
    try:
        response = requests.get(f"{OLLAMA_API_URL}/tags")
        return response.json()
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 