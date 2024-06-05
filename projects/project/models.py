from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry

from projects.db import Base


class Project(Base):
    __tablename__ = 'projects_data'

    project_id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer)  # foreign key to what?
    name: str = Column(String(200))
    description: str = Column(String)
    geometry: Geometry = Column(Geometry(geometry_type='POLYGON'))

    def __init__(self, user_id: int, name: str, description: str, geometry: Geometry):
        self.user_id = user_id
        self.name = name
        self.description = description
        self.geometry = geometry
