import yaml
from fastapi.openapi.utils import get_openapi
from rich import print

from .main import app


def generate_openapi_schema_file():
    print("[magenta]Generating OpenAPI schema file[/magenta]")
    with open("schema.yaml", "w") as f:
        openapi_json = get_openapi(
            title=app.title,
            version=app.version,
            openapi_version=app.openapi_version,
            description=app.description,
            routes=app.routes,
        )
        yaml.dump(openapi_json, f)
    print("[cyan]OpenAPI schema.yaml file generated[/cyan]")


if __name__ == "__main__":
    generate_openapi_schema_file()
