from fastapi import FastAPI

app = FastAPI(title= "Prompt Library API")

@app.get("/")
def root():
    return {"message" : "Prompt Library API running"}
