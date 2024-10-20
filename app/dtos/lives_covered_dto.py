# from app.enums.enums import Category, FamilyMember, Relationship
# from pydantic import BaseModel, Field, constr, condecimal
# from typing import Optional
# from datetime import datetime

# class LivesCoveredDto(BaseModel):
#     category: Optional[Category] = None
#     relationship: Relationship
#     family_member: Optional[FamilyMember] = None
#     title: constr(strict=True) = Field(..., description="Title of the beneficiary")  # type: ignore
#     first_name: constr(strict=True) = Field(..., description="First name of the beneficiary") # type: ignore
#     last_name: constr(strict=True) = Field(..., description="Last name of the beneficiary") # type: ignore
#     date_of_birth: constr(regex=r'^\d{2}-\d{2}-\d{4}$') = Field(..., description="Date of birth in dd-mm-yyyy format") # type: ignore
#     nationality: constr(strict=True) = Field(..., description="Nationality of the beneficiary") 
#     botswana_id: Optional[constr(strict=True)] = Field(None, description="Botswana ID of the beneficiary") # type: ignore
#     cover_amount: Optional[condecimal(gt=0)] = Field(None, description="Cover amount for the beneficiary") # type: ignore
#     is_student: Optional[bool] = Field(None, description="Indicates if the beneficiary is a student")
#     has_special_needs: Optional[bool] = Field(None, description="Indicates if the beneficiary has special needs")

#     def get_current_age(self) -> int:
#         today = datetime.now()
#         day, month, year = map(int, self.date_of_birth.split('-'))
#         birth_date = datetime(year, month, day)

#         age = today.year - birth_date.year
#         if (today.month, today.day) < (birth_date.month, birth_date.day):
#             age -= 1
#         return age


import re  # Add this line
from app.enums.enums import Category, FamilyMember, Relationship
from pydantic import BaseModel, Field, constr, condecimal, validator
from typing import Optional
from datetime import datetime

class LivesCoveredDto(BaseModel):
    category: Optional[Category] = None
    relationship: Relationship
    familyMember: Optional[FamilyMember] = None
    title: constr(strict=True) = Field(..., description="Title of the beneficiary")
    firstName: constr(strict=True) = Field(..., description="First name of the beneficiary")
    lastName: constr(strict=True) = Field(..., description="Last name of the beneficiary")
    dateOfBirth: constr(strict=True) = Field(..., description="Date of birth in dd-mm-yyyy format")  # Updated
    nationality: constr(strict=True) = Field(..., description="Nationality of the beneficiary")
    botswanaId: Optional[constr(strict=True)] = Field(None, description="Botswana ID of the beneficiary")
    coverAmount: Optional[condecimal(gt=0)] = Field(None, description="Cover amount for the beneficiary")
    isStudent: Optional[bool] = Field(None, description="Indicates if the beneficiary is a student")
    hasSpecialNeeds: Optional[bool] = Field(None, description="Indicates if the beneficiary has special needs")

    @validator('dateOfBirth')
    def validate_date_of_birth(cls, value):
        if not re.match(r'^\d{2}-\d{2}-\d{4}$', value):
            raise ValueError('Date of birth must be in dd-mm-yyyy format')
        return value

    def get_current_age(self) -> int:
        today = datetime.now()
        day, month, year = map(int, self.date_of_birth.split('-'))
        birth_date = datetime(year, month, day)

        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    class Config:
        use_enum_values = True