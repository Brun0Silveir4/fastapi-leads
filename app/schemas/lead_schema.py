from pydantic import BaseModel

class LeadCreate(BaseModel):
    name: str
    email: str
    phone: str
    
class LeadResponse(BaseModel):
    id: str
    name: str 
    email: str 
    created_at: str 