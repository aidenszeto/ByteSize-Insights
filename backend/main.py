from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import github, users, auth
from emails import create_html

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(github.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(create_html.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
