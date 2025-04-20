from sqlalchemy.orm import Session

from src.models import WalletRequest


def create_request(db: Session, address: str, balance: float, bandwidth: int, energy: int):
    db_request = WalletRequest(
        wallet_address=address,
        balance=balance,
        bandwidth=bandwidth,
        energy=energy
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request


def get_requests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(WalletRequest).offset(skip).limit(limit).all()
