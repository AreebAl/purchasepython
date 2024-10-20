# app/controllers/purchase_controller.py
from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.dtos.purchase_dto import PurchaseDto
from app.service.purchase_service import PurchaseService

# Define the Blueprint for the purchase controller
purchase_blueprint = Blueprint('purchase', __name__)

# Create an instance of the service
purchase_service = PurchaseService()

@purchase_blueprint.route('/purchase', methods=['POST'])
def create_purchase():
    try:
        # Parse and validate the incoming request data
        data = request.json
        print(data, "from request data")

        # Validate using the PurchaseDto
        purchase_dto = PurchaseDto(**data)

        # Process the purchase using the service
        processed_purchase = purchase_service.process_purchase(purchase_dto)

        # Ensure processed_purchase is serializable (convert to dict if necessary)
        response_data = processed_purchase.dict() if isinstance(processed_purchase, PurchaseDto) else processed_purchase

        # Return the response as JSON
        return jsonify({"success": True, "data": response_data}), 200

    except ValidationError as e:
        # Handle validation errors and return them as JSON
        return jsonify({
            "success": False, 
            "error": "Validation error", 
            "details": e.errors()  # e.errors() is a list of validation issues, which is JSON serializable
        }), 400

    except Exception as e:
        # Handle any other generic errors
        return jsonify({"success": False, "error": str(e)}), 500