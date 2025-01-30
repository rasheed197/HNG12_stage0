from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:80",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReturnData(BaseModel):
    email: str
    current_datetime: str
    github_url: str

@app.get("/")
async def root() -> ReturnData:
    now = datetime.now()
    iso_string_without_microseconds = now.isoformat().split('.')[0]
    print(type(iso_string_without_microseconds))
    return JSONResponse(
        content={
            "email": "tiamiyurasheed.tr@gmail.com",
            "current_datetime": iso_string_without_microseconds,
            "github_url": "https://github.com/rasheed197/HNG12"
        },
        status_code=status.HTTP_200_OK
    )