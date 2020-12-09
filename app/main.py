from typing import List

from fastapi import Depends, FastAPI, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware

import datetime
import json
import pandas

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{params}")
def main(symbol: str = Path(..., title=" The params which user want to get status")):
    result = {"status":"status","message":"message"}
    return result
