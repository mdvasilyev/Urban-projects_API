from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from starlette.responses import Response

from projects import db

from . import schema
from . import services

router = APIRouter(prefix="/v1/projects", tags=["projects"])


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schema.Project])
async def get_all_projects(database: Session = Depends(db.get_db)):
    return await services.get_all_projects(database)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.Project)
async def create_project(request: schema.ProjectPost, database: Session = Depends(db.get_db)):
    return await services.create_project(request, database)


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_project(project_id: int, database: Session = Depends(db.get_db)):
    return await services.delete_project(project_id, database)


@router.put("/{project_id}", status_code=status.HTTP_202_ACCEPTED, response_model=schema.Project)
async def update_project(project_id: int, database: Session = Depends(db.get_db)):
    return await services.update_project(project_id, database)
