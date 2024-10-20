from pydantic import BaseModel, EmailStr, Field, constr, validator
from typing import Optional
from datetime import date
from app.enums.enums import AccountType  # Adjust this import based on your structure
# from app.utility.date_util import validate_date_string  # Assuming you have a similar validation function
from .address_dto import AddressDto  # Adjust import as necessary
from .employment_details_dto import EmploymentDetailsDto  # Adjust import as necessary


class PersonalDetailsDto(BaseModel):
    title: str = Field(..., description="Title of the person")
    firstName: str = Field(..., description="First name of the person")
    lastName: str = Field(..., description="Last name of the person")
    nationality: str = Field(..., description="Nationality of the person")
    botswanaIdNumber: str = Field(..., description="Botswana ID number")
    
    dateOfBirth: date = Field(..., description="Date of birth in dd-mm-yyyy format", 
                                 example="15-08-1990")
    idExpiryDate: str = Field(..., description="ID expiry date in dd-mm-yyyy format", 
                                 example="15-08-2025")

    isPip: bool = Field(..., description="Indicates if PIP (Personal Independence Payment) is applicable")
    email: EmailStr = Field(..., description="Email address")
    contactNumber: str = Field(..., description="Contact number")

    residentialAddress: AddressDto = Field(..., description="Residential address")
    postalAddress: AddressDto = Field(..., description="Postal address")
    
    previousResidentialAddress: Optional[AddressDto] = Field(None, 
        description="Optional previous residential address")
    
    employmentDetails: EmploymentDetailsDto = Field(..., description="Employment details")

    class Config:
        use_enum_values = True
