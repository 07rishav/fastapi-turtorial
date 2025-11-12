from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# ✅ Allow requests from Google
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Allowed origins (Google in your case)
    allow_credentials=True,      # Allows cookies, authorization headers
    allow_methods=["*"],         # Allows all HTTP methods
    allow_headers=["*"],         # Allows all headers
)

# ✅ Routers
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# ✅ Root route
@app.get("/")
def root():
    return {"message": "Hello world!!"}
