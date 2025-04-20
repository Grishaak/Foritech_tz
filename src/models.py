from sqlalchemy import Column, Integer, String, Float, DateTime
from src.database import Base
from datetime import datetime


class WalletRequest(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    wallet_address = Column(String(42), index=True)
    timestamp = Column(DateTime, default=datetime.now)
    balance = Column(Float)
    bandwidth = Column(Integer)
    energy = Column(Integer)
