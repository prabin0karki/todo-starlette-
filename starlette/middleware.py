from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware
from auth.middleware import BasicAuthBackend

middleware = [
    Middleware(AuthenticationMiddleware, backend=BasicAuthBackend()),
    Middleware(GZipMiddleware),
    Middleware(CORSMiddleware, allow_origins=["*"]),
    # ...
]
