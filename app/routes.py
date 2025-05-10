# views.py

from flask import Blueprint, request, render_template, url_for, redirect, flash, session
from scraper import scrape_website


# Create a Blueprint for the main application
main_bp = Blueprint('main', __name__, template_folder='templates')  # Define blueprint with the name 'main'


@main_bp.route('/<number_of_articles>', methods=['GET', 'POST'])
def home(number_of_articles):
    """ This function will increase the number of articles to scrape """


    return "Hello, World!"  # Render the home page with a simple message)