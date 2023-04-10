from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, func, Text, DateTime


class AssemblyUnit(Base):
    __tablename__ = 'AssemblyUnit'
    Id = Column(Integer, primary_key=True)  # ключ
    Code = Column(String)  # обозначение детали
    Name = Column(String)  # наименование детли
    Description = Column(Text)  # поле примечания
    AssemblyUnitTypeId = Column(Integer)  # поле с номером тип ДСЕ (изделие, узел, деталь)
    AssemblyUnitGroupId = Column(Integer)  # поле с ид папки в котором находиться ДСЕ
    IsDeleted = Column(Integer)  # поле с меткой о том удалена ДСЕ или нет (1 значит удалена)
    IntegrationId = Column(Text)  # какое-то поле для интеграции
    AttachedFilePathList = Column(Text)  #
    DefaultSpecificationId = Column(Integer)
    RowAddDate = Column(DateTime)
    RowAddUser = Column(Text)
    RowUpdateDate = Column(DateTime)
    RowUpdateUser = Column(Text)


if __name__ in '__main__':
    session = SessionLocal()
    query = session.query(AssemblyUnit.Name) \
        .limit(10) \
        .all()
    print(query)
