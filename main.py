#!/usr/bin/env python3

from fastapi import FastAPI
from tools.mosdef_tool import MosdDEF as tool_mosdef

app = FastAPI()

@app.get("/")
def root():
    return { "data": "hello world from FastAPI!" }

@app.post("/api/tool/mosdef")
def mosdef(data):
    return { "data": tool_mosdef(data) }
