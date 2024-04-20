from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

'''

class Usuarios(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user_text = Column(String, index=True)

class Eventos(Base):
    __tablename__ = 'eventos'

    id = Column(Integer, primary_key=True, index=True)
    evento_text = Column(String, index=True)

class Inscricoes(Base):
    __tablename__ = 'inscricoes'

    id = Column(Integer, primary_key=True, index=True)
    inscricao_text = Column(String, index=True)
    evento_id = Column(Integer, ForeignKey("eventos.id"))

'''