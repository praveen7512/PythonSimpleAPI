from fastapi import FastAPI

app = FastAPI()

@app.get("/notes")
def read_root():
    return {"message": "Hello, World!"}




