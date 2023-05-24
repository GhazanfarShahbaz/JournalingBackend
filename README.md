# Journaling Backend
### This is the backend for my journaling application. It uses FastAPI with the Tortoise ORM

# Installation
```
git clone https://github.com/GhazanfarShahbaz/JournalingBackend
cd JournalingBackend
virtualenv env 
source env/bin/activate
python3 -m pip install -r requirements.txt
```

# Running this Application
### ## Although I use systemctl to run my app and then portforward it, to run this execute the command below
```
uvicorn app.main:app --reload
```

# Usage
### Once the app is running, you can access the default endpoint at http://127.0.0.1:8000/. It returns a JSON with the message {"Hello": "World"}

# Adding Endpoints
### To add more endpoints, simply add a new function to the app.main module and decorate it with the appropriate decorator, such as @app.get, @app.post, etc.
### Here is an example of a function that returns a JSON containing a "message" string. This function has the decorater get, so it only responds to get requests.
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/newEndpoint")
def read_root():
    return {"message": "You just created a new endpoint"}
```