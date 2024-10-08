from flask import Blueprint

genai = Blueprint('genai',__name__)

from app import cache
from .routes import register_routes

register_routes(genai,cache)