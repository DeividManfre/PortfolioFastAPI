from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .schemas import SaleCreate, SaleUpdate, SaleInDB, SaleListResponse
from .controller import create_sale, get_sale, get_sales, update_sale, delete_sale
from utils.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sales/", response_model=SaleInDB)
async def create_sale_handler(sale: SaleCreate, db: Session = Depends(get_db)):
    return create_sale(db, sale)

@router.get("/sales/{sale_id}", response_model=SaleInDB)
async def read_sale(sale_id: int, db: Session = Depends(get_db)):
    sale = get_sale(db, sale_id)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

@router.get("/sales/", response_model=SaleListResponse)
async def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sales = get_sales(db, skip, limit)
    return {"sales": sales}

@router.put("/sales/{sale_id}", response_model=SaleInDB)
async def update_sale_handler(sale_id: int, sale_update: SaleUpdate, db: Session = Depends(get_db)):
    sale = update_sale(db, sale_id, sale_update)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

@router.delete("/sales/{sale_id}", response_model=dict)
async def delete_sale_handler(sale_id: int, db: Session = Depends(get_db)):
    sale = get_sale(db, sale_id)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    delete_sale(db, sale_id)
    return {"message": "Sale deleted"}
