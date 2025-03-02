from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name':'Sahil'}}

@app.get('/aboutData')
def index():
    return {'data': 'about Page'}


if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8005, reload=True)