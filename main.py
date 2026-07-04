from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get():
    return {"message": "This is my FastAPI app"}

@app.get("/view")
def view():
    students = [
        {
            "id": 1,
            "name": "Hiral",
            "age": 20,
            "course": "BSC DS"
        },
        {
            "id": 2,
            "name": "Smriti",
            "age": 20,
            "course": "BSC AI"
        },
        {
            "id": 3,
            "name": "Pranjali",
            "age": 20,
            "course": "BSC IT"
        }
    ]

    return students