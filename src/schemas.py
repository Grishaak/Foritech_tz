from pydantic import BaseModel
from datetime import datetime


class WalletInfoRequest(BaseModel):
    address: str


class WalletInfoResponse(BaseModel):
    balance: float
    bandwidth: int
    energy: int


class RequestHistoryItem(BaseModel):
    wallet_address: str
    timestamp: datetime
    balance: float

    class Config:
        from_attributes = True
