from sqlalchemy.orm import Session
from .models import Sale
from .schemas import SaleCreate, SaleUpdate, SaleInDB

def create_sale(db: Session, sale: SaleCreate) -> SaleInDB:
    _sale = Sale(**sale.dict())
    db.add(_sale)
    db.commit()
    db.refresh(_sale)
    return _sale

def get_sale(db: Session, sale_id: int) -> SaleInDB:
    return db.query(Sale).filter(Sale.id == sale_id).first()

def get_sales(db: Session, skip: int = 0, limit: int = 100) -> list[SaleInDB]:
    return db.query(Sale).offset(skip).limit(limit).all()

def update_sale(db: Session, sale_id: int, sale_update: SaleUpdate) -> SaleInDB:
    _sale = get_sale(db, sale_id)
    for field, value in sale_update.dict(exclude_unset=True).items():
        setattr(_sale, field, value)
    db.commit()
    db.refresh(_sale)
    return _sale

def delete_sale(db: Session, sale_id: int) -> None:
    _sale = get_sale(db, sale_id)
    db.delete(_sale)
    db.commit()
