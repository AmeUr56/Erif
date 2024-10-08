from flask import Blueprint

main = Blueprint('main',__name__)

from app import cache
from .routes import register_routes

register_routes(main,cache)