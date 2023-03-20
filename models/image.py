from database import Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String, ForeignKey

# ---- these are SQL models (tables)
# map between users and roles


class InstagramImage(Base):
    __tablename__ = 'images'
    id = Column(Integer(), primary_key=True)
    user_id = Column('user_id', Integer(), ForeignKey('user.id'))
    user = relationship()
    image_url = Column(String(), nullable=False)
