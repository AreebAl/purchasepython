
# from pydantic import BaseModel, Field, conlist
# from typing import List, Optional
# from enum import Enum
# from app.dtos.beneficiary_details_dto import BeneficiaryDetailsDto
# from app.dtos.benefits_dto import BenefitsDto
# from app.dtos.personal_details_dto import PersonalDetailsDto
# from app.enums.enums import CoverType
# from app.dtos.lives_covered_dto import LivesCoveredDto
# from app.dtos.payment_details_dto  import PaymentDetailsDto

# class PurchaseDto(BaseModel):
#     cover_type: CoverType = Field(..., description="Type of coverage")
#     personal_details: PersonalDetailsDto = Field(..., description="Personal details of the applicant")
#     lives_covered: conlist(LivesCoveredDto, min_items=1) = Field(..., description="List of lives covered") # type: ignore
#     beneficiaries: conlist(BeneficiaryDetailsDto, min_items=1) = Field(..., description="List of beneficiaries")
#     payment_details: Optional[PaymentDetailsDto] = Field(None, description="Optional payment details")
#     upload_documents: Optional[List[UploadDocumentsDto]] = Field(None, description="Optional list of documents to upload") # type: ignore
#     confirm_details: bool = Field(..., description="Confirmation of the provided details")
#     benifit: BenefitsDto = Field(..., description="Benefits associated with the purchase")



from pydantic import BaseModel, Field, validator
from typing import List, Optional
from enum import Enum
from app.dtos.beneficiary_details_dto import BeneficiaryDetailsDto
from app.dtos.benefits_dto import BenefitsDto
from app.dtos.personal_details_dto import PersonalDetailsDto
from app.enums.enums import CoverType
from app.dtos.lives_covered_dto import LivesCoveredDto
from app.dtos.payment_details_dto import PaymentDetailsDto
from app.dtos.upload_documents_dto import UploadDocumentsDto
class PurchaseDto(BaseModel):
    coverType: CoverType = Field(..., description="Type of coverage")
    personalDetails: PersonalDetailsDto = Field(..., description="Personal details of the applicant")
    livesCovered: List[LivesCoveredDto] = Field(..., description="List of lives covered")
    beneficiaries: List[BeneficiaryDetailsDto] = Field(..., description="List of beneficiaries")
    paymentDetails: Optional[PaymentDetailsDto] = Field(None, description="Optional payment details")
    uploadDocuments: Optional[List[UploadDocumentsDto]] = Field(None, description="Optional list of documents to upload")
    confirmDetails: bool = Field(..., description="Confirmation of the provided details")
    benifit: BenefitsDto = Field(..., description="Benefits associated with the purchase")

    @validator('livesCovered')
    def check_lives_covered_min_items(cls, v):
        if len(v) < 1:
            raise ValueError('At least one life must be covered.')
        return v

    @validator('beneficiaries')
    def check_beneficiaries_min_items(cls, v):
        if len(v) < 1:
            raise ValueError('At least one beneficiary must be provided.')
        return v

    class Config:
        # This ensures that enum values are serialized as strings
        use_enum_values = True
        
    