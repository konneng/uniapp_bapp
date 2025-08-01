from fastapi import FastAPI
from . import models, database
from .routes import router
from .routes_protocols import router as protocols_router  # ✅ nuovo import

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()
app.include_router(router)
app.include_router(protocols_router)  # ✅ nuovo router
