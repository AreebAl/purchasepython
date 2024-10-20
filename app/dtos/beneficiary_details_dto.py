# from marshmallow import Schema, fields, validate, ValidationError
# from datetime import datetime

# # Custom validation function for date format
# def validate_date_format(date_str):
#     try:
#         datetime.strptime(date_str, "%d-%m-%Y")
#     except ValueError:
#         raise ValidationError("Invalid date format. Expected dd-mm-yyyy.")

# class BeneficiaryDetailsDto(Schema):
#     name = fields.String(required=True)
#     lastName = fields.String(required=True)
#     nationalId = fields.String(required=True)
#     nationality = fields.String(required=True)

#     # Custom date validation
#     dateOfBirth = fields.String(required=True, validate=validate_date_format)

#     relationship = fields.String(required=True)  # Replace with EnumField if using enums
#     email = fields.Email(allow_none=True)
#     gender = fields.String(allow_none=True)
#     mobileNumber = fields.String(allow_none=True)

#     city = fields.String(allow_none=True)
#     postalCode = fields.String(allow_none=True)
#     countryCode = fields.String(allow_none=True)


from pydantic import BaseModel, Field, EmailStr, constr, validator
from datetime import datetime
from typing import Optional

class BeneficiaryDetailsDto(BaseModel):
    name: constr(strict=True) = Field(..., description="Beneficiary's first name")
    lastName: constr(strict=True) = Field(..., description="Beneficiary's last name")  # Use snake_case for fields
    nationalId: constr(strict=True) = Field(..., description="National ID of the beneficiary")
    nationality: constr(strict=True) = Field(..., description="Nationality of the beneficiary")
    
    # Custom date validation
    dateOfBirth: constr(strict=True) = Field(..., description="Date of birth in dd-mm-yyyy format")

    relationship: constr(strict=True) = Field(..., description="Relationship of the beneficiary")  # Replace with Enum if needed
    email: Optional[EmailStr] = Field(None, description="Email address of the beneficiary")
    gender: Optional[constr(strict=True)] = Field(None, description="Gender of the beneficiary")
    mobileNumber: Optional[constr(strict=True)] = Field(None, description="Mobile number of the beneficiary")
    
    city: Optional[constr(strict=True)] = Field(None, description="City of residence")
    postalCode: Optional[constr(strict=True)] = Field(None, description="Postal code of the beneficiary's address")
    countryCode: Optional[constr(strict=True)] = Field(None, description="Country code of the beneficiary's address")

    @validator('dateOfBirth')
    def validate_date_format(cls, date_str):
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Invalid date format. Expected dd-mm-yyyy.")
        return date_str

    class Config:
        use_enum_values = True