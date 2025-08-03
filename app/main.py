from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models, database
from .routes import router
from .routes_protocols import router as protocols_router  # ✅ nuovo import

# Crea tutte le tabelle definite nei modelli
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# ✅ Middleware CORS per abilitare il frontend React a connettersi

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- accetta tutte le origini
    allow_credentials=False,  # <-- importante!
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Includi i router FastAPI
app.include_router(router)
app.include_router(protocols_router)
