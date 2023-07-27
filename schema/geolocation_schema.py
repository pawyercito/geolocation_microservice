from pydantic import BaseModel


class RevGeocode(BaseModel):
    lat: float
    lng: float