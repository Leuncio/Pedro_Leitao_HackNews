# views.py

from flask import Blueprint, request, render_template
from .scraper import URL, number_of_articles


# Create a Blueprint for the main application
main_bp = Blueprint('main', __name__, template_folder='templates')  # Define blueprint with the name 'main'


@main_bp.route('/', methods=['GET', 'POST'])
@main_bp.route('/<int:numero>', methods=['GET', 'POST'])
def home(numero=1):
    """Render the home page with a list of articles."""
    articles = number_of_articles(URL, numero)
    return render_template('index.html', articles=articles)
