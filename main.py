#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import BaseModel
from tools.mosdef_tool import MosdDEF as tool_mosdef

class DataMosdef(BaseModel):
    name: str
    smiles: str
    length: float
    count: int

app = FastAPI()

@app.get("/")
def root():
    return { "data": "hello world from FastAPI!" }

@app.post("/api/tool/mosdef")
def mosdef(data: DataMosdef):
    return { "data": tool_mosdef(data) }
