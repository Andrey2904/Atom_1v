from fastapi import FastAPI, Path

from typing import Annotated

from items_views import router as items_router
from users.views import router as users_router



app = FastAPI()
app.include_router(items_router, tags=["items"])
app.include_router(users_router, tags=["users"])
@app.get("/")
def hello_index():
    return{
        "message": "Hi index 1",
        "email":"sv_dron@examial",
    }


