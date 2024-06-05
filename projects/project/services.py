from typing import List, Type
from binascii import unhexlify
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from shapely import wkb, from_wkt, to_wkb

from . import models
from . import schema
from . import validator
from .models import Project


def generate_geometry(coordinates: List[List[List[float]]]) -> str:
    res = []
    for pair in coordinates[0]:
        res.append(f'{pair[0]} {pair[1]}')
    return ','.join(res)


async def create_project(request: schema.ProjectPost, db: Session) -> schema.Project:
    project = await validator.project_validator(db, request.name)
    if project:
        raise HTTPException(status_code=400, detail="Project already exists")
    new_project = models.Project(user_id=request.user_id, name=request.name,
                                 description=request.description, geometry=request.geometry)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


async def get_all_projects(db: Session) -> List[models.Project]:
    projects = db.query(models.Project).all()
    return projects


async def delete_project(project_id: int, db: Session):
    db.query(models.Project).filter(models.Project.project_id == project_id).delete()
    db.commit()


async def update_project(project_id: int, request: schema.ProjectPost, db: Session):
    project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    project.name = request.name
    project.description = request.description
    geometry = from_wkt(f'{request.geometry.type}(({generate_geometry(request.geometry.coordinates)}))')
    project.geometry = to_wkb(geometry, hex=True)
    db.add(project)
    db.commit()
    db.refresh(project)
    return project
