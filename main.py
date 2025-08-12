#!/usr/bin/env python3

from fastapi import FastAPI
from tools.mosdef_tool import MosdDEF as tool_mosdef

app = FastAPI()

@app.post("/api/tool/mosdef")
def mosdef(data):
    return tool_mosdef(data)
