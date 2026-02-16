"""
Main class of the application.
All configuration below is used for Controller additions, cors configuration,
Swagger and Redoc headers, etc.
"""
from fastapi import FastAPI

from src.middleware import register_middleware

tags_metadata = [
    {
        "name": "Prediction",
        "description": "Methods responsible for managing data and make predictions",
    }
]

app = FastAPI(
    version='1.0.0',
    title='Tech Challenge 05 - Datathon',
    description='A Rest API collection for FIAP - Tech Challenge',
    terms_of_service='#',
    license_info={"name": "Apache 2.0", "url": "https://www.apache.org/licenses/LICENSE-2.0"},
    redoc_url='/documentation/redoc',
    docs_url='/documentation/swagger',
    openapi_url='/documentation/openapi.json',
    openapi_tags=tags_metadata
)

register_middleware(app)
