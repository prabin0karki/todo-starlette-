import httpx
from starlette.staticfiles import StaticFiles

# from starlette.templating import JinjaTemplates


client = httpx.AsyncClient()

# templates = JinjaTemplates(directory=str(settings.TEMPLATES_DIR))

# static = StaticFiles(directory=str(settings.STATIC_DIR))
