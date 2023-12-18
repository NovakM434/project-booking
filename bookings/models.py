from sqlalchemy import Column, Integer, String, JSON, ForeignKey, Date, \
    Computed

from database import Base

class Rooms(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey('hotels.id'))
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)


class Bookings(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True)
    room_id = Column(ForeignKey('rooms.id'))
    user_id = Column(ForeignKey('users.id'))
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed('(date_to - date_from) * price'))
    total_days = Column(Integer, Computed('(date_to - date_from)'))