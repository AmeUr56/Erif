from flask import Blueprint

ts = Blueprint('ts',__name__)

from app import cache
from .routes import register_routes

register_routes(ts,cache)