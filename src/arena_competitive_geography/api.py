# API FastAPI pour le moteur Arena Competitive Geography
import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from genesis_core import ResultContract
from .analyzer import analyze_territory

app = FastAPI(
    title="Arena Competitive Geography API",
    description="Moteur d'Analyse de Géographie Concurrentielle",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil avec carte d'emprise concurrentielle
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Arena API - Interface non trouvee</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "engine": "Arena", "version": "1.0.0"}

@app.get("/api/v1/territory", response_model=ResultContract)
def get_territory(lat: float = Query(48.8566), lon: float = Query(2.3522)):
    return analyze_territory(lat, lon)
