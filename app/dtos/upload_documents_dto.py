from pydantic import BaseModel, Field, constr, conint
from typing import Optional

class UploadDocumentsDto(BaseModel):
    documentType: constr(min_length=1, strip_whitespace=True) = Field(..., description="Type of the document") # type: ignore
    fileName: constr(min_length=1, strip_whitespace=True) = Field(..., description="Name of the file") # type: ignore
    fileType: Optional[str] = Field(None, description="Optional file type")
    fileSize: Optional[conint(ge=0)] = Field(None, description="Optional file size in bytes")  # Must be non-negative
    url: constr(min_length=1, strip_whitespace=True) = Field(..., description="enter url here")  # type: ignore
# Example usage (uncomment for testing)
# upload_document = UploadDocumentsDto(
#     document_type="Identity Proof",
#     file_name="passport.jpg",
#     file_type="image/jpeg",
#     file_size=2048
# )
# print(upload_document)
