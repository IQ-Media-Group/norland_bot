import datetime

from sqlalchemy import Table, Column, Integer, String, MetaData, JSON, BigInteger, DateTime, ForeignKey, Boolean, Text

metadata_obj = MetaData()


tg_users = Table(
    "tg_users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("tg_id", BigInteger, unique=True),
    Column("FIO", Text, nullable=True),
    Column("email", Text, nullable=True),
    Column("phone", Text, nullable=True),
)
