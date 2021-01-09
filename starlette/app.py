from starlette.applications import Starlette
import uvicorn
from middleware import middleware
from routes import routes
from database import on_startup, on_shutdown
from starlette.config import Config

config = Config(".env")


app = Starlette(
    routes=routes,
    debug=config("DEBUG"),
    middleware=middleware,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
