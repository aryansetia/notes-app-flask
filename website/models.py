from . import db  
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from datetime import datetime 
import pytz 
from typing import List


IST = pytz.timezone("Asia/Kolkata")



class User(db.Model, UserMixin): 
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] =  mapped_column(String(150))
    password: Mapped[str] = mapped_column(String(150))
    first_name: Mapped[str] = mapped_column(String(150))
    notes: Mapped[List["Note"]] = relationship() 

# one to many - that means one user can create multiple notes 
class Note(db.Model): 
    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str] = mapped_column(String(10000))
    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(IST))

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id")) # note attached to a specific user.id   