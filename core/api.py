from fastapi import Request, HTTPException
from fastapi.routing import APIRouter
from utils.quote_storage import load_quotes, save_quotes, get_next_id

from fastapi.middleware.cors import CORSMiddleware
import random
import os

API_KEY = os.getenv("API_KEY", "supersecretkey")
router = APIRouter()

@router.get("/")
def read_root():
    # Default fetch
    return {"message": "QUOTES GET YA MOTIVATIONAL QUOTES HERE!"}

@router.get("/quotes")
def get_random_quote():
    # Loads all quotes and fetches random quote
    quotes = load_quotes()
    return random.choice(quotes)

@router.get("/quotes/{quote_id}")
def get_quote_by_id(quote_id: int):
    # Fetches a quote by it's id
    quotes = load_quotes()
    for quote in quotes:
        if quote["id"] == quote_id:
            return quote
    raise HTTPException(status_code=404, detail="Quote not found")

@router.post("/quotes")
def add_quote(request: Request, quote: dict):
    # Adds new quote to the dataset (KEY REQUIRED IN HEADER)
    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    quotes = load_quotes()
    quote["id"] = get_next_id(quotes)
    quotes.append(quote)
    save_quotes(quotes)
    return {"message": "Quote added!", "quote": quote}

@router.put("/quotes/{quote_id}")
def update_quote(quote_id: int, updated_quote: dict, request: Request):
    # Updates existing quote by its ID (KEY REQUIRED IN HEADER)
    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    quotes = load_quotes()
    for i, quote in enumerate(quotes):
        if quote["id"] == quote_id:
            updated_quote["id"] = quote_id
            quotes[i] = updated_quote
            save_quotes(quotes)
            return {"message": "Quote updated", "quote": updated_quote}
    raise HTTPException(status_code=404, detail="Quote not found")

@router.delete("/quotes/{quote_id}")
def delete_quote(quote_id: int, request: Request):
    # Delete quote by its ID (KEY REQUIRED IN HEADER)
    if request.headers.get("x-api-key") != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    quotes = load_quotes()
    for quote in quotes:
        if quote["id"] == quote_id:
            quotes.remove(quote)
            save_quotes(quotes)
            return {"message": "Quote deleted"}
    raise HTTPException(status_code=404, detail="Quote not found")

def setup_routes(app):
    # CORS setup
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router)
