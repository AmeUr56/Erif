from flask import Blueprint

nlp = Blueprint('nlp',__name__)

from app import cache
from .routes import register_routes

register_routes(nlp,cache)