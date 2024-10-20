# from marshmallow import Schema, fields, validate

# class AddressDto(Schema):
#     addressLine1 = fields.String(required=False, allow_none=True)
#     addressLine2 = fields.String(required=False, allow_none=True)
#     addressLine3 = fields.String(required=False, allow_none=True)
#     addressLine4 = fields.String(required=False, allow_none=True)
#     addressLine5 = fields.String(required=False, allow_none=True)
#     addressLine6 = fields.String(required=False, allow_none=True)
#     city = fields.String(required=True)
#     country = fields.String(required=True)
#     postalCode = fields.String(required=False, allow_none=True)
#     countryCode = fields.String(required=False, allow_none=True)

from pydantic import BaseModel
from typing import Optional

class AddressDto(BaseModel):
    addressLine1: Optional[str] = None
    addressLine2: Optional[str] = None
    addressLine3: Optional[str] = None
    addressLine4: Optional[str] = None
    addressLine5: Optional[str] = None
    addressLine6: Optional[str] = None
    city: str
    country: str
    postalCode: Optional[str] = None
    countryCode: Optional[str] = None
