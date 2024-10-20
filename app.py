from flask import Flask
from app.controller.purchase_controller import purchase_blueprint  # Import your controllers

# Initialize the Flask app
app = Flask(__name__)

# Register blueprints for controllers
app.register_blueprint(purchase_blueprint)  # Assuming you're using Flask blueprints for controllers

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
