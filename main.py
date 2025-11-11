from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser les connexions de l'application mobile
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/identify")
async def identify(file: UploadFile):
    # Pour l'instant, on simule la reconnaissance
    # On renvoie un film exemple
    return {
        "title": "Inception",
        "overview": "Un voleur qui dérobe des secrets à travers les rêves est chargé d'une mission inédite.",
        "release_date": "2010-07-16",
        "poster_path": "https://image.tmdb.org/t/p/w500/qmDpIHrmpJINaRKAfWQfftjCdyi.jpg"
    }
