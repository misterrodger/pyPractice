from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from pydantic import BaseModel, Field, ValidationError
from typing import Optional

app = Flask(__name__)

client = Elasticsearch("http://localhost:9200")


class QueryParams(BaseModel):
    name: str
    age: int
    location: str


@app.route("/")
def hello():
    return "Ok I'm running"


@app.route("/friend")
def get_friends():
    try:
        params = "ok"

    except ValidationError as e:
        return jsonify({"error": e.errors()}), 422
