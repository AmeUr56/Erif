from flask import Blueprint

rl = Blueprint('rl',__name__)

from app import cache
from .routes import register_routes

register_routes(rl,cache)