class LeadModel:
    def __init__(self, name: str, email: str, phone: str, created_at: str):
        self.name = name,
        self.email = email,
        self.phone = phone,
        self.created_at = created_at
        
    def to_dict(self):
        return{
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "created_at": self.created_at
        }