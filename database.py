from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, INTEGER, String, create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:@localhost/justq?charset=utf8', convert_unicode=False)
Session = sessionmaker()
Base = declarative_base()
session = Session(bind=engine)


class Order(Base):
    __tablename__ = 'data'

    # Column 정의
    id = Column(INTEGER, primary_key=True)
    orderdate = Column(String)
    region = Column(String)
    rep = Column(String)
    item = Column(String)
    units = Column(INTEGER)
    unit_cost = Column(INTEGER)
    east_regula = Column(String)
    total = Column(INTEGER)


# Representation
def columnInformation(self):
    return "<Order(" \
           "OrderData='%s', " \
           "Region='%s', " \
           "Rep='%s', " \
           "Item='%s'," \
           "Units='%d'," \
           "Unit_Cost='%f'" \
           "East_Regula='%s'" \
           "Total='%f')>" % \
           (
               self.OrderData,
               self.Region,
               self.Rep,
               self.Item,
               self.Units,
               self.Unit_Cost,
               self.East_Regula,
               self.total
           )


# DB Insert Method
def insertData(ORDERDATE, REGION, REP, ITEM, UNITS, UNIT_COST, EAST_REGULA, TOTAL):
    Add_Order = Order(orderdate=ORDERDATE,
                      region=REGION,
                      rep=REP,
                      item=ITEM,
                      units=UNITS,
                      unit_cost=UNIT_COST,
                      east_regula=EAST_REGULA,
                      total=TOTAL
                      )
    session.add(Add_Order)
    session.commit()
