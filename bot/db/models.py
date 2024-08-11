from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from bot.db.base import Base


class User(Base):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)
