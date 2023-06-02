from sqlalchemy import Column, Integer, String
from app.db.base import Base


class Contact(Base):
    __tablename__ = "contact"

    email = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    phone = Column(String)
    website = Column(String)
