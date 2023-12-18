from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
from bookings.router import router as router_bookings

app = FastAPI()
app.include_router(router_bookings) # очевидно регистрация роутера


