from fastapi import Depends, FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException
from src.dependencies import get_token_header
from src.internal import admin
from src.routers.api import router as router_api
from src.config import API_PREFIX, ALLOWED_HOSTS
from src.routers.handlers.http_error import http_error_handler


def get_application() -> FastAPI:
    application = FastAPI(
        swagger_ui_parameters={"defaultModelsExpandDepth": -1}
    )

    application.include_router(router_api, prefix=API_PREFIX)

    application.add_exception_handler(HTTPException, http_error_handler)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(
        admin.router,
        prefix="/admin",
        tags=["admin"],
        dependencies=[Depends(get_token_header)],
        responses={418: {"description": "I'm a teapot. Coffee is denied, since your token is an apple"}},
    )

    return application


app = get_application()
