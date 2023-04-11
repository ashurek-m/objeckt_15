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
    Priority = Column(Integer)  # приоритет (низкий-3, нормальный-2, высокий-1, наивысший-0) обезательно поле
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
    Name = Column(String)  # Наименование МЛ обязательное поле
    Description = Column(Text)  # примечания
    WorkflowStatusId = Column(Integer)  # неизвестно (идентификатор состояния рабочего процесса)
    AssemblyUnitSpecificationId = Column(Integer)  # Id спецификации по которой изготавиваем ДСЕ обязательное поле
    IntegrationId = Column(Text)  # что-то для интеграции
    ProductionOrderId = Column(Integer)  # Id заказа
    Series = Column(Text)  # неизвестно
    DtFactFrom = Column(DateTime)  # фактическая дата
    DtFactTo = Column(DateTime)  # фактическая дата
    DtForecastFrom = Column(DateTime)  # прогнозная дата
    DtForecastTo = Column(DateTime)  # прогнозная дата
    DtPlanFrom = Column(DateTime)  # планируемая дата начала изготовления
    DtPlanTo = Column(DateTime)  # планируемая дата завершения изготовления
    Priority = Column(Integer)  # приоритет (низкий-3, нормальный-2, высокий-1, наивысший-0) обязательное поле
    CurrentSatusId = Column(Integer)  # производственный статус
    NumberStr = Column(Text)  # номер МЛ (item) обязательное поле
    DecimalPartPlanCount = Column(Float)  # планируемое кол-во обязательное поле
    ParentId = Column(Integer)  # неизвестно
    RowAddDate = Column(DateTime)  # дата создания строки в БД
    RowAddUser = Column(Text)  # кто создал
    RowUpdateDate = Column(DateTime)  # дата последнего изменения строки в БД
    RowUpdateUser = Column(Text)  # кто изменил
    CurrentOperationId = Column(Integer)  # id текущей операции
    DeptId = Column(Integer)  # неизвестно
    DtPlanEnd = Column(DateTime)  # неизвестно
    DtPlanStart = Column(DateTime)  # неизвестно
    Number = Column(Integer)  # неизвестно
    PartPlanCount = Column(Integer)  # неизвестно
