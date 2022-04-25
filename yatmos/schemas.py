from typing import Optional, List

from pydantic import BaseModel


class TestSuiteBase(BaseModel):
    title: str
    desc: Optional[str] = None


class TestSuiteCreate(TestSuiteBase):
    pass


class TestSuite(TestSuiteBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    title: str
    desc: Optional[str] = None

    class Config:
        schema_extra = {"example": {"title": "YATMoS Backend", "desc": "YATMoS backend tests"}}


class ProjectCreate(ProjectBase):
    pass


class UpdateProject(BaseModel):
    title: Optional[str]
    desc: Optional[str]

    class Config:
        schema_extra = {"example": {"title": "YATMoS Backend", "desc": "YATMoS backend API tests"}}


class Project(ProjectBase):
    id: int
    test_suites: List[TestSuite] = []

    class Config:
        orm_mode = True
