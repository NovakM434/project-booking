from sqlalchemy import select

from bookings.models import Bookings
from database import async_session_maker

#сюда перенесем логику всего что связано с бд
#общий класс для всех запросов. Т.е если мы хотим получить все записи
# какой-то модели, то используем этот класс, просто подставляю нужную модель
# получается в роутере нам просто нужно будет подставить модель, вместо того
# чтобы писать весь этот код

class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query =  select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_ore_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by): #объявили методом букингдао, теперь
        # можем #
        # вызвать его в другом файле.
        async with async_session_maker() as session:  # асинхронная функция
            query = select(cls.model).filter_by(**filter_by)  # орм заапрос
            result = await session.execute(query)  # делаем орм запрос в
            # переменную
            return result.scalars().all()  # отдаем ответ. на самом деле там
            # изначально ответ не json но фастапи сам его трансформирует в json
