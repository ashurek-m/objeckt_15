from database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, Float


class ProductionOrder(Base):
    __tablename__ = 'ProductionOrder'
    Id = Column(Integer, primary_key=True)
    OrderNum = Column(String)  # number order
    StatusTypeId = Column(Integer)  # неизвестная фигня
    DtOrder = Column(DateTime)  # дата создания заказа
    Name = Column(Text)  # Название заказа
    IntegrationId = Column(Text)  # поле для интеграции
    CustomerName = Column(Text)  # контрагент
    DtFactFrom = Column(DateTime)  # дата фактического начала изготовления
    DtFactTo = Column(DateTime)  # дата фактического окончания выполнения
    DtForecastFrom = Column(DateTime)  # дата начала работ прогноз
    DtForecastTo = Column(DateTime)  # дата окончания работ прогноз
    DtOrderShipment = Column(DateTime)  # дата отгрузка
    DtPlanFrom = Column(DateTime)  # дата начало работ план
    DtPlanTo = Column(DateTime)  # дата окончания работ план
    Priority = Column(Integer)  # приоритет (низкий-3, нормальный-2, высокий-1, наивысший-0)
    CurrentStatusId = Column(Integer)  # производственный статус
    Description = Column(Text)  # примечания
    RowAddDate = Column(DateTime)  # дата создания строки в БД
    RowAddUser = Column(Text)  # кто создал
    RowUpdateDate = Column(DateTime)  # дата последнего изменения строки в БД
    RowUpdateUser = Column(Text)  # кто изменил
    DtFromFact = Column(DateTime)  # неизвестно
    DtFromPlan = Column(DateTime)  # неизвестно
    DtToFact = Column(DateTime)  # неизвестно
    DtToPlan = Column(DateTime)  # неизвестно


class WorkflowChart(Base):
    __tablename__ = 'WorkflowChart'
    Id = Column(Integer, primary_key=True)
    Name = Column(String)
    Description = Column(Text)
    WorkflowStatusId = Column(Integer)
    AssemblyUnitSpecificationId = Column(Integer)
    IntegrationId = Column(Text)
    ProductionOrderId = Column(Integer)
    Series = Column(Text)
    DtFactFrom = Column(DateTime)
    DtFactTo = Column(DateTime)
    DtForecastFrom = Column(DateTime)
    DtForecastTo = Column(DateTime)
    DtPlanFrom = Column(DateTime)
    DtPlanTo = Column(DateTime)
    Priority = Column(Integer)
    CurrentSatusId = Column(Integer)
    NumberStr = Column(Text)
    DecimalPartPlanCount = Column(Float)
    ParentId = Column(Integer)
    RowAddDate = Column(DateTime)
    RowAddUser = Column(Text)
    RowUpdateDate = Column(DateTime)
    RowUpdateUser = Column(Text)
    CurrentOperationId = Column(Integer)
    DeptId = Column(Integer)
    DtPlanEnd = Column(DateTime)
    DtPlanStart = Column(DateTime)
    Number = Column(Integer)
    PartPlanCount = Column(Integer)
