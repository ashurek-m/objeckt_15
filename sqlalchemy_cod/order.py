from database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime


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
