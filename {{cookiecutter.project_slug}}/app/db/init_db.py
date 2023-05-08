from app.models.base import Example
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def init_examples(db: AsyncSession) -> None:
    currency = await db.scalars(select(Example).limit(1))
    if currency.first():
        return
    db.add_all(
        [
            Example(title="example1"),
            Example(title="example2"),
        ]
    )
    await db.commit()


async def init_db(db: AsyncSession) -> None:
    await init_examples(db)
