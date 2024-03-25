from flask import Flask
from azure_devops.routes import azure_devops_bp
from extensions import db

def create_app():
    app = Flask(__name__)

    # For SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
    # To silence the deprecation warning
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    

    # Load configuration from a config file/environment variables
    # app.config.from_object('config.ConfigClassName')

    # Register blueprints
    app.register_blueprint(azure_devops_bp, url_prefix='/azure-devops')

    # Set up logging (optional)
    # import logging
    # logging.basicConfig(level=logging.INFO)

    # Global error handlers (optional)
    # app.register_error_handler(404, not_found_error)
    # app.register_error_handler(500, internal_error)

    return app

# Function to run the app (for development)
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Set debug=False in production
