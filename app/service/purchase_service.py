# app/services/purchase_service.py
from app.dtos.purchase_dto import PurchaseDto

class PurchaseService:
    def process_purchase(self, purchase_data: PurchaseDto) -> PurchaseDto:
        # Business logic for processing the purchase would go here
        # For now, let's return the same purchase data as an example.
        print(purchase_data,"from the purchase service")
        return purchase_data
