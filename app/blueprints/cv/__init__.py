from flask import Blueprint

cv = Blueprint('cv',__name__)

from app import cache
from .routes import register_routes

register_routes(cv,cache)