# views.py

from flask import Blueprint, request, render_template, url_for, redirect, flash, session
from .scraper import number_of_articles


# Create a Blueprint for the main application
main_bp = Blueprint('main', __name__, template_folder='templates')  # Define blueprint with the name 'main'


@main_bp.route('/<number_of_articles>', methods=['GET', 'POST'])
def home(number_of_articles):

    articles = number_of_articles
    
    return articles