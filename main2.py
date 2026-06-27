from fastapi import FastAPI

# Create FastAPI app with metadata
app = FastAPI(
    title="My First FastAPI App",
    description="This is a simple FastAPI application for learning purposes.",
    version="1.0.0"
)

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to My First FastAPI App!"
    }

# About endpoint
@app.get("/about")
def about():
    return {
        "app": "My First FastAPI App",
        "version": "1.0.0",
        "description": "This is a simple FastAPI application for learning purposes."
    }

# Example GET endpoint
@app.get("/hello/{name}")
def say_hello(name: str):
    return {
        "message": f"Hello, {name}!"
    }

# Example POST endpoint
@app.post("/items/")
def create_item(item: dict):
    return {
        "message": "Item created successfully",
        "item": item
    }