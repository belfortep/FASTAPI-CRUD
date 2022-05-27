from fastapi import FastAPI
from routes.user import user
#para utilizar servidor es uvicorn app:app --reload para que reinicie solo
app = FastAPI() 

app.include_router(user)
     
