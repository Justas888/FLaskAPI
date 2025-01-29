from pydantic import BaseModel
import datetime

class AutomobilisSchema(BaseModel):
    id: int
    gamintojas: str
    modelis: str
    spalva: str
    kaina: float
    kaina_su_pvm: float
    sukurimo_data: datetime.datetime

    class Config:
        from_attributes = True
