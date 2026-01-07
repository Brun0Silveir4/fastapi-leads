from app.core.database import database
from bson import ObjectId 

collection = database["leads"]

class LeadRepository:
    
    async def create(self, data: dict) -> str:
        result = await collection.insert_one(data)
        return str(result.inserted_id)
    
    async def find_all(self) -> list[dict]:
        leads = []
        
        async for lead in collection.find():
            lead_id = str(lead["_id"])
            del lead["_id"]
            ordered_lead = {
                "id": lead_id,
                **lead 
            }
            leads.append(ordered_lead)
        return leads 
    
    async def find_by_id(self, lead_id: str) -> dict | None:
        lead = await collection.find_one({"_id": ObjectId(lead_id)})
        
        if not lead:
            return None
        
        lead_id = str(lead["_id"])
        del lead["_id"]
        
        return {"id": lead_id, **lead}
    
    async def delete(self, lead_id: str) -> None:
        await collection.delete_one({"_id": ObjectId(lead_id)})