from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from loguru import logger
from pydantic.error_wrappers import ValidationError
from starlette.requests import Request
from src.schema.custom_response import CustomResponse
from fastapi.openapi.utils import get_openapi
import fastapi.openapi.utils as fu
import os
import logging
import sys

from uvicorn import Config, Server

app = FastAPI()

# and override the schema
fu.validation_error_response_definition = {
    "title": "HTTPValidationError",
    "type": "object",
    "properties": {
        "detail": {"title": "Validation error message", "type": "string"},
    },
}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
) -> JSONResponse:
    """
    item_id value is not a valid interger
    q field required
    """
    error_message = "\n".join(f"{x['loc'][1]} {x['msg']}" for x in exc.errors())
    res = CustomResponse(success=True, message=error_message)
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=res.dict())


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: int):
    # logger = logging.getLogger("uvicorn.access")
    g_log = logging.getLogger(__name__)
    g_log.info("get item")
    logging.getLogger(__name__).info("in1234")
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}


@app.on_event("startup")
async def startup_event():

    logging.root.handlers = []
    logging.root.setLevel(logging.DEBUG)
    for name in logging.root.manager.loggerDict.keys():
        print(name)
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    g_log = logging.getLogger(__name__)
    uv_access_log = logging.getLogger("uvicorn.access")

    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
        )
    )
    g_log.addHandler(handler)
    g_log.setLevel(logging.DEBUG)
    uv_access_log.addHandler(handler)
    uv_access_log.setLevel(logging.DEBUG)
    g_log.info("start")
