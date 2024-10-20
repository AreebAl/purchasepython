# from marshmallow import Schema, fields, validate, ValidationError

# class BenefitsDto(Schema):
#     premiumPaidUp = fields.Boolean(required=True, error_messages={"required": "premiumPaidUp is required."})
#     cashBack = fields.Boolean(required=True, error_messages={"required": "cashBack is required."})


from pydantic import BaseModel, Field

class BenefitsDto(BaseModel):
    premiumPaidUp: bool = Field(..., description="Indicates if the premium is paid up")  # Required field
    cashBack: bool = Field(..., description="Indicates if cash back is applicable")  # Required field
