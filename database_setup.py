import sys
from  sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

class Restaurant(base):
	__tablename__ = 'restaurant'

class MenuItem(base):
	__tablename__ = 'menu_item'



Base = declarative_base()
# insert at end of file

engine = create_engine('sqlite://restaurantmenu.db')

Base.metadata.create_all(engine)
