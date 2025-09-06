from fastapi import FastAPI

app = FastAPI()

@app.get('/')
@app.get('/home')
def home():
    return {"message": "This is home page"}