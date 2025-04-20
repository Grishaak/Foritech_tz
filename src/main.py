from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from tronpy import Tron

from src.database import engine, get_db, Base
from src.logic_db import create_request, get_requests

from src.schemas import WalletInfoResponse, WalletInfoRequest, RequestHistoryItem

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/wallet-info", response_model=WalletInfoResponse)
async def get_wallet_info(
        request: WalletInfoRequest,
        db: Session = Depends(get_db)
):
    try:
        client = Tron()
        address = request.address

        if not client.is_address(address):
            raise HTTPException(status_code=400, detail="Invalid address")

        account = client.get_account(address)
        balance_sun = client.get_account_balance(address)
        balance = balance_sun / 1_000_000

        bandwidth = account.get('free_net_usage', 0) if account else 0
        energy = account.get('account_resource', {}).get('energy_usage', 0) if account else 0

        create_request(db, address, balance, bandwidth, energy)

        return {
            "balance": balance,
            "bandwidth": bandwidth,
            "energy": energy
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/requests-history", response_model=list[RequestHistoryItem])
def get_history(
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
):
    return get_requests(db, skip=skip, limit=limit)
