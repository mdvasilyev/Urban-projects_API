from typing import List
from pydantic import BaseModel, Field


class Geometry(BaseModel):
    type: str = Field(default="Polygon")
    coordinates: List[List[List[float]]]


class Project(BaseModel):
    project_id: int = Field(primary_key=True)
    user_id: int
    name: str
    description: str
    geometry: Geometry


class ProjectPost(BaseModel):
    user_id: int
    name: str
    description: str
    geometry: Geometry
