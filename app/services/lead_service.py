from app.repositories.lead_repository import LeadRepository 
from app.models.lead_model import LeadModel
from datetime import datetime, timezone

class LeadService:
    
    def __init__(self):
        self.repo = LeadRepository()
        
    async def create_lead(self, data: dict):
        lead = LeadModel(
            name=data["name"],
            email=data["email"],
            phone=data["phone"],
            created_at=datetime.now(timezone.utc).isoformat()
        )
        
        return await self.repo(lead.to_dict())
    
    async def list_leads(self):
        return await self.repo.find_all()
    
    async def get_lead(self, lead_id: str):
        return await self.repo.find_by_id(lead_id)
    
    async def delete_lead(self, lead_id: str):
        return await self.repo.delete(lead_id)