#!/usr/bin/env python3

from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from tools.mosdef_tool import MosdDEF as tool_mosdef
from tools.packmol_moltemplate_tool import packmol_template_tool as tool_packmol_template

class DataMosdef(BaseModel):
    name: str
    smiles: str
    length: float
    count: int

class DataPackmolMoltemplate(BaseModel):
    names: List[str]
    count: List[int]
    lenght: int

app = FastAPI()

@app.get("/")
def root():
    return { "data": "hello world from FastAPI!" }

@app.post("/api/tool/mosdef")
def mosdef(data: DataMosdef):
    d = {
            "name": data.name,
            "smiles": data.smiles,
            "length": data.length,
            "count": data.count
    }
    return { "data": tool_mosdef(d) }

@app.post("/api/tool/template")
def mosdef(data: DataPackmolMoltemplate):
    d = {
            "names": data.name,
            "count": data.count,
            "length": data.length
    }
    return { "data": tool_packmol_template(d) }
