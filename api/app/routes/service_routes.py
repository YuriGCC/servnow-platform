from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from api.app.db.session import get_db
from api.app.models.service import Service
from api.app.models.service import Service
from api.app.schemas.service import ServiceCreate, ServiceRead

router = APIRouter()

@router.post('/services/', response_model=ServiceRead)
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    db_service = db.query(Service).filter(Service.name == service.name).first()

    if db_service:
        raise HTTPException(status_code=400, detail='Serviço já existe')

    new_service = Service(name=service.name, price=service.price)
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service

@router.get('/services/{service_id}', response_model=ServiceRead)
def read_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=400, detail='Serviço não encontrado')
    return service

@router.put('/services/{service_id}', response_model=ServiceRead)
def update_service(service_id: int, service_update: ServiceCreate, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()

    if not service:
        raise HTTPException(status_code=400, detail='Serviço não encontrado')
    service.name = service_update.name
    service.price = service_update.price
    db.commit()
    db.refresh(service)
    return service

@router.delete('/services/{service_id')
def delete_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=400, detail='Serviço não encontrado')

    db.delete(service)
    db.commit()
    return {'detailhe': 'Serviço deletado'}
