from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func, Text, DateTime


class AssemblyUnit(Base):
    __tablename__ = 'AssemblyUnit'
    Id = Column(Integer, primary_key=True)
    Code = Column(String)
    Name = Column(String)
    Description = Column(Text)
    AssemblyUnitTypeId = Column(Integer)
    AssemblyUnitGroupId = Column(Integer)
    IsDeleted = Column(Integer)
    IntegrationId = Column(Text)
    AttachedFilePathList = Column(Text)
    DefaultSpecificationId = Column(Integer)
    RowAddDate = Column(DateTime)
    RowAddUser = Column(Text)
    RowUpdateDate = Column(DateTime)
    RowUpdateUser = Column(Text)


if __name__ in '__main__':
    session = SessionLocal()
    query = session.query(AssemblyUnit.Name)\
        .limit(10)\
        .all()
    print(query)
