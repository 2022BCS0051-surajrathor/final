from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {
        "Name": "Suraj Rathor",
        "Roll No": "2022BCS0051"
    }

@app.get("/predict")
def predict():
    return {
        "prediction": "dummy",
        "Name": "Suraj Rathor",
        "Roll No": "2022BCS0051"
    }