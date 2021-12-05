from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status
from pydantic.error_wrappers import ValidationError
from starlette.requests import Request
from .schema.custom_response import CustomResponse
from fastapi.openapi.utils import get_openapi
import fastapi.openapi.utils as fu


app = FastAPI()

# and override the schema
fu.validation_error_response_definition = {
    "title": "HTTPValidationError",
    "type": "object",
    "properties": {
        "detail": {"title": "Validation error message", "type": "string"},
    },
}

fu.validation_error_response_definition


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
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, content=res.dict()
    )


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}
