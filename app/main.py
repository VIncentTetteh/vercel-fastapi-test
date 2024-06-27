from fastapi import FastAPI

app = FastAPI(title="Test api")

@app.get("/",status_code=200)
def main():
    return {"message":"welcome to test app"}