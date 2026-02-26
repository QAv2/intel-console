"""FastAPI application — Intel Console."""

from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from server.db import init_db, close_db
from server.routers import entities, relationships, sources, graph, tags


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()


app = FastAPI(title="Intel Console", version="0.1.0", lifespan=lifespan)

# Routers
app.include_router(entities.router)
app.include_router(relationships.router)
app.include_router(sources.router)
app.include_router(graph.router)
app.include_router(tags.router)

# Static files
STATIC_DIR = Path(__file__).parent.parent / "static"
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/")
async def index():
    return FileResponse(str(STATIC_DIR / "index.html"))
