from fastapi import FastAPI
from fastapi.exceptions import HTTPException

app = FastAPI()

@app.get('/content')
def get_content():
    return 'Some data returned from our API'

#@app.get('/content')
#def get_content_from_file():
#    path = './content/content.txt'
#    try:
#        with open(path, 'r') as f:
#            content = f.read()
#        return content
#    except Exception as e:
#        raise HTTPException(500, f'Error: {e}')
