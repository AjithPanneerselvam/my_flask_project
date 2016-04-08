# Start of config code
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
#end of config code

# Class definitions
class Shelter(Base):
	__tablename__ = 'shelter'

	name = Column(String(30),nullable = False)
	address = Column(String(50),nullable = False)
	city = Column(String(20))
	state = Column(String(20))
	zipCode = Column(String(15))
	website = Column(String(30))
	id = Column(Integer,primary_key=True)

class Puppy(Base):
	name = Column(String(30),nullable=False)
	date of birth = Column(String(20))
	gender = Column(String(7))
	weight = Column(String(10))
	shelter_id = Column(Integer,ForeignKey('shelter.id'))
	shelter = relationship(Shelter)

# insert at end of file
engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)

