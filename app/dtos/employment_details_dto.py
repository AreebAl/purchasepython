# from marshmallow import Schema, fields, validate

# class EmploymentDetailsDto(Schema):
#     status = fields.String(required=True, error_messages={"required": "status is required."})
#     occupation = fields.String(required=True, error_messages={"required": "occupation is required."})
#     sourceOfIncome = fields.String(required=True, error_messages={"required": "sourceOfIncome is required."})


from pydantic import BaseModel, Field, constr

class EmploymentDetailsDto(BaseModel):
    status: constr(min_length=1, max_length=100) = Field(..., description="Employment status", error_messages={"required": "status is required."})
    occupation: constr(min_length=1, max_length=100) = Field(..., description="Occupation", error_messages={"required": "occupation is required."})
    sourceOfIncome: constr(min_length=1, max_length=100) = Field(..., description="Source of income", error_messages={"required": "sourceOfIncome is required."})

    class Config:
        # Optionally set any additional Pydantic configuration here
        anystr_strip_whitespace = True  # Optional: Strips whitespace from strings
