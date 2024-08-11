from datetime import datetime
from typing import Annotated

from sqlalchemy import BigInteger, String
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)

from bot.config_reader import config

created_at = Annotated[datetime, mapped_column(default=datetime.now)]
str_256 = Annotated[str, 256]
intpk = Annotated[int, mapped_column(BigInteger, primary_key=True)]

updated_at = Annotated[
    datetime,
    mapped_column(
        default=datetime.now,
        onupdate=datetime.now,
    ),
]


class Base(DeclarativeBase):
    id: Mapped[intpk]
    created_at: Mapped[created_at]
    # created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[updated_at]
    type_annotation_map = {str_256: String(256)}

    # repr_cols_num = 3
    repr_cols = tuple()

    def __repr__(self):
        """Relationships не используются в repr(), т.к. могут вести к неожиданным подгрузкам"""
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            # if col in self.repr_cols or idx < self.repr_cols_num:
            cols.append(f"{col}={getattr(self, col)}")

        return f"<{self.__class__.__name__} {', '.join(cols)}>"


print(type(config.db_url_async))
print(config.db_url_async)

engine = create_async_engine(url=str(config.db_url_async), echo=True)
sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
