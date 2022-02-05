from fastapi import FastAPI
from fastapi.exceptions import HTTPException

app = FastAPI()

@app.get('/')
def get_content():
    return 'Some data returned from our API'
