import sys
from  sqlalchemy import Column, ForeignKey, Integer, String
from sqla[A[D[D[D[D[C[[B[C[C[C[Cchemy[D[D[D[D[Dlchemy[2~.ext.declarative import_base[D[D[D[D[D declarattive_base[D[D[D[D[D[D[D[D[D[3~[3~[C[C[[[C[C[C[C[C[Cive_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()
# insert at end of file

engine = create_engine('sqlite://restaurantmenu.db')

Base.metadata.create_all(engine)
