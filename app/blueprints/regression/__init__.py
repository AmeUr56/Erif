from flask import Blueprint

regression = Blueprint('regression',__name__)

from app import cache
from .routes import register_routes

register_routes(regression,cache)