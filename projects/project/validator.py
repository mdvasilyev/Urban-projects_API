from typing import Optional
from sqlalchemy.orm import Session

from .models import Project


async def project_validator(db_session: Session, name: Project.name) -> Optional[Project]:
    return db_session.query(Project).filter(Project.name == name).first()
