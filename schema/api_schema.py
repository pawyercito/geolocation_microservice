from pydantic import BaseModel, Field


class ApiResponse(BaseModel):
    code: int
    message: str
    success: bool
    data: dict
    external_transaction_id: str = Field("fcea920f7412b5da7be0cf42b8c93759", description="external transaction id")
    internal_transaction_id: str = Field(..., description="internal transaction id")
    channel: str = Field("Development", description="channel")
