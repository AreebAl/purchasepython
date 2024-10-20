from pydantic import BaseModel, Field, constr, conint
from app.enums.enums import AccountType  # Adjust the import based on your project structure

class PaymentDetailsDto(BaseModel):
    bankName: str = Field(..., description="Name of the bank")
    branchName: str = Field(..., description="Name of the bank branch")
    accountHolderName: str = Field(..., description="Name of the account holder")
    accountNumber: constr(min_length=5, max_length=22) = Field(..., description="Account number") # type: ignore
    accountType: AccountType = Field(..., description="Type of the account")
    debitOrderDate: conint(ge=1, le=31) = Field(..., description="Date for debit order") # type: ignore
    confirmDetails: bool = Field(..., description="Confirmation of the details")

    class Config:
        use_enum_values = True