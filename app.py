# /// script 
# requires-python = ">=3.12"
# dependencies = [
#          "fastapi",
#          "uvicorn",
#          "requests",
# ]
# ///

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware (
    CORSMiddleware,
    allow_orgin = ['*'],
    allow_credentials = True,
    allow_methods = ['GET', 'POST'],
    allow_headers = ['*']
)

@app.get("/")
def home():
    return{"Text to be displayed"}


if ___name__ == '__main__':
    import uvicorn
    uvicorn.run (app, host="0.0.0.0", port=8000)