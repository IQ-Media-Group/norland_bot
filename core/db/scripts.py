from core.db.database import engine
from core.db.models import metadata_obj
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.sql import select
from core.db.models import tg_users


def create_tables():
    metadata_obj.create_all(engine)


create_tables()


def create_user(tg_id: int, fio: str, email: str, phone: str) -> None:
    with engine.connect() as conn:
        stmt = insert(tg_users).values(
            [
                {
                    "tg_id": tg_id,
                    "FIO": fio,
                    "email": email,
                    "phone": phone
                }
            ]
        ).on_conflict_do_nothing()
        conn.execute(stmt)
        conn.commit()


def get_user(tg_id: int) -> dict:
    with engine.connect() as conn:
        stmt = select(tg_users).where(tg_users.c.tg_id == tg_id)
        return conn.execute(stmt).fetchone()
