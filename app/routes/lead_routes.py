from fastapi import APIRouter, HTTPException
from app.schemas.lead_schema import LeadCreate
from app.services.lead_service import LeadService

router = APIRouter(prefix="/leads", tags=["leads"])
service = LeadService()

@router.post("/")
async def create_lead(lead: LeadCreate):
    try:
        lead_id = await service.create_lead(lead.model_dump())
        return {"id": lead_id, "message": "Lead created sucessfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
async def list_leads():
    leads = await service.list_leads()
    
    if not leads:
        raise HTTPException(status_code=404, detail="unregistered leads")
    
    return leads

@router.get("/{lead_id}")
async def get_lead(lead_id: str):
    lead = await service.get_lead(lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead 

@router.delete("/{lead_id}")
async def delete_lead(lead_id: str):
    leadToDelete = await delete_lead(lead_id)

    if not leadToDelete:
        raise HTTPException(status_code=404, detail="Lead doesn't exists to delete")
    
    return leadToDelete
