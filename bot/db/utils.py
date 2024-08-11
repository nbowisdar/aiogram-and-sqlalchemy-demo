import asyncio

from bot.db.base import engine, sessionmaker
from bot.db.models import Base, User


# Function to create the tables
async def create_tables():
    async with engine.begin() as conn:
        # Use the async engine to create all tables
        await conn.run_sync(Base.metadata.create_all)


async def drop_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def test():
    async with sessionmaker() as session:

        # Crete new user
        user = User(id=286365412, name="Test", phone="123456789")
        session.add(user)
        print(f"User added with id: {user.id}")

        # test update
        # stmt = select(User).filter_by(phone="123456789")
        # result = await session.execute(stmt)
        # user = result.scalar_one()
        # user.name = "Updated Name"

        await session.commit()


if __name__ == "__main__":
    # asyncio.run(create_tables())
    asyncio.run(test())
