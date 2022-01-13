from flask import Blueprint, render_template
from flask import current_app as app
from application.controller.inventory_api import fetch_products


# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
)


@home_bp.route('/', methods=['GET'])
def home():
    """Homepage."""
    return render_template(
        'index.html',
        title='Shopify Backend Challenge',
        subtitle='Following Best Practices to build Scalable Web Applications.',
        template='home-template',
    )