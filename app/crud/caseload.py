import logging

import models
import schemas
from sqlalchemy.orm import Session


def get_caseload(db: Session, caseload_id: int):
    return db.query(models.Caseload).filter(models.Caseload.id == caseload_id).first()


def create_caseload(db: Session, caseload: schemas.CaseloadCreate):
    db_caseload = models.Caseload()
    [setattr(db_caseload, i[0], i[1]) for i in caseload]
    db.add(db_caseload)
    db.commit()
    db.refresh(db_caseload)
    return db_caseload


def delete_caseload(db: Session, caseload_id: int):
    db_caseload = get_caseload(db, caseload_id)
    if db_caseload:
        db.delete(db_caseload)
        db.commit()
        return True
    else:
        return False


def update_caseload(db: Session, caseload_id: int, updated_caseload: schemas.CaseloadCreate):
    db_caseload = get_caseload(db, caseload_id)
    if db_caseload is None:
        return False

    [setattr(db_caseload, i[0], i[1]) for i in updated_caseload]
    db.commit()
    db.refresh(db_caseload)
    return True