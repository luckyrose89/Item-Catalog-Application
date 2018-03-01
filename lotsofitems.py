from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Items, User

engine = create_engine('sqlite:///itemcatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy user
User1 = User(name="Anna Barista", email="AnnaT67@udacity.com",
             picture='https://i.imgur.com/G661sAt.png')
session.add(User1)
session.commit()

# Create four dummy categories to populate catalog
# Add one or two items to each category
category1 = Category(name="Cakes",
                     picture="https://i.imgur.com/Uf6TYcx.jpg",
                     user_id=1)

session.add(category1)
session.commit()

category2 = Category(name="Cookies",
                     picture="https://i.imgur.com/l72wRjn.jpg",
                     user_id=1)

session.add(category2)
session.commit()

category3 = Category(name="Pies",
                     picture="https://i.imgur.com/ZG4H6mZ.jpg",
                     user_id=1)

session.add(category3)
session.commit()

category4 = Category(name="Breads",
                     picture="https://i.imgur.com/E7Vyu24.jpg",
                     user_id=1)

session.add(category4)
session.commit()

# Create dummy items to populate categories

item1 = Items(name="Cheesecake",
              image="https://i.imgur.com/bo6rjEd.jpg",
              price="$25.00",
              description="Our speciality",
              category_id=1,
              user_id=1)

session.add(item1)
session.commit()

item2 = Items(name="Red Velvet Cake",
              image="https://i.imgur.com/LC2HpHh.jpg",
              price="$30.00",
              description="Creamy delight",
              category_id=1,
              user_id=1)

session.add(item2)
session.commit()

item3 = Items(name="Choco-chip cookie",
              image="https://i.imgur.com/tCiXG6k.jpg",
              price="$2.50",
              description="The cookie with lots of chips",
              category_id=2,
              user_id=1)

session.add(item3)
session.commit()

item4 = Items(name="Pecan Pie",
              image="https://i.imgur.com/NLCfTKQ.jpg",
              price="$28.00",
              description="A classic dessert",
              category_id=3,
              user_id=1)

session.add(item4)
session.commit()

item5 = Items(name="Apple Pie",
              image="https://i.imgur.com/wzsTZ5V.jpg",
              price="$20.00",
              description="Made fresh on request",
              category_id=3,
              user_id=1)

session.add(item5)
session.commit()

item6 = Items(name="bagel",
              image="https://i.imgur.com/XYffiEX.jpg",
              price="$1.25",
              description="A hit with customers",
              category_id=4,
              user_id=1)

session.add(item6)
session.commit()


print("Added catalog items!")
