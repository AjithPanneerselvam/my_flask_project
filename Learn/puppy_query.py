from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from puppies import Base, Shelter, Puppy
#from flask.ext.sqlalchemy import SQLAlchemy
from random import randint
import datetime
import random


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


def query_one():
    """Query all of the puppies and return the results in ascending alphabetical order"""
    result = session.query(Puppy.name).order_by(Puppy.name.asc()).all()

    # print the result with puppy name only
    # print len(result)
    for item in result:
        print item[0]


def query_two():
    """Query all of the puppies that are less than 6 months old organized by the youngest first"""
    today = datetime.date.today()
    result = session.query(Puppy.name, Puppy.dateOfBirth).order_by(Puppy.dateOfBirth.desc()).all()

    # print the result with puppy name and dob
    for item in result:
        puppy_months = diff_month(today, item[1])
        if puppy_months < 6:
            print "{name}: {months}".format(name=item[0], months=puppy_months)

def query_three():
    """Query all puppies by ascending weight"""
    result = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight.asc()).all()

    for item in result:
        print item[0], item[1]

def query_four():
    """Query all puppies grouped by the shelter in which they are staying"""
    result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
    for item in result:
        print item[0].id, item[0].name, item[1]


# Helpers methods
def diff_month(d1, d2):
    """calculate number of months by counting day from today"""
    delta = d1 - d2
    return delta.days / 30

query_one()
query_two()
query_three()
query_four()