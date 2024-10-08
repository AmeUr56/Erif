from flask import Blueprint

classification = Blueprint('classification',__name__)

from app import cache
from .routes import register_routes

register_routes(classification,cache)