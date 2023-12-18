from fastapi import APIRouter
from sqlalchemy import select

from bookings.dao import BookingDAO
from bookings.models import Bookings
from bookings.schemas import SBooking
from database import async_session_maker

router = APIRouter(
    prefix="/bookings", # изначальный префикс
    tags=["Бронирование"], # тут название роутера
)

@router.get("")
async def get_bookings() -> list[SBooking]:# тут мы указываем схему,
    print(await BookingDAO.find_all())
    # и в документации нам покажут, что должно вернутся
    return await BookingDAO.find_all()