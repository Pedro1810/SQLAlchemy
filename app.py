from sqlalchemy import create_engine, Column, Integer, String, or_, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

engin = create_engine('sqlite:///data.db')
Session = sessionmaker(bind=engin)
session = Session()
Base = declarative_base()

class Goods(Base):

    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    quantity = Column(Integer)

class Customers(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(Integer)

Base.metadata.create_all(engin)

def addGood(title, quantity):
    good = Goods(title=title, quantity=quantity)
    session.add(good)
    session.commit()

def addCustomers(name, age, gender):
    customer = Customers(name=name, age=age, gender=gender)
    session.add(customer)
    session.commit()

# addGood('Велосипед', 18)
# addGood('Самокат', 15)
# addGood('Скейт', 31)
# addGood('Сноуборд', 38)

# addCustomers('Саша', 18, 1)
# addCustomers('Оля', 20, 0)
# addCustomers('Никита', 10, 1)
# addCustomers('Ван', 14, 1)
# addCustomers('Ира', 22, 0)
# addCustomers('Сергей', 12, 1)
# addCustomers('Михаил', 15, 1)
# addCustomers('Михаил', 20, 1)

customers_man_over_18 = session.query(Customers).filter(Customers.age > 18, Customers.gender == 1)
customers_under_5 = session.query(Customers).filter(func.length(Customers.name) < 5)
customers_mikhail = session.query(Customers).filter(Customers.name == 'Михаил', Customers.age < 17)

# goods_list = session.query(Goods).filter(or_(Goods.quantity > 20, Goods.id == 1))
for row in customers_man_over_18:
    print(row.name, row.age, row.gender)
print('='*20)
for row in customers_under_5:
    name = row.name
    if len(name) < 5:
        print(row.name, row.age, row.gender)
print('=' * 20)
for row in customers_mikhail:
    print(row.name, row.age, row.gender)
print('='*20)