# views.py

from flask import Blueprint, request, render_template, url_for, redirect, flash, session

# Create a Blueprint for the main application
main_bp = Blueprint('main', __name__, template_folder='templates')  # Define blueprint with the name 'main'

@main_bp.route('/', methods=['GET', 'POST'])
def home():

    return "Hello, World!"  # Render the home page with a simple message)