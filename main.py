from fastapi import FastAPI

app = FastAPI()


@app.get("/internal/{route}")
async def root():
    return {"message": "Hello World"}