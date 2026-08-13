import uuid
from datetime import date,datetime
from decimal import Decimal
from sqlalchemy import (
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Text,
    Uuid,
    Enum,
)
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy.sql.expression import text
from app.utils.enums.currency_type import CurrencyType
from app.utils.enums.transaction_type import TransactionType

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id:Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    email:Mapped[str] = mapped_column(
        String,
        unique=True,
        nullable=False
    )
    password:Mapped[str] = mapped_column(
        String,
        nullable=False
    )
    created_at:Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text('now()')
    )
    accounts:Mapped[list["Account"]] = relationship(back_populates="user")

class Account(Base):
    __tablename__ = "accounts"
    id:Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    name:Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    balance:Mapped[Decimal] = mapped_column(
        Numeric(12,2),
        nullable=False,
        default=Decimal("0.00")
    )
    currency:Mapped[CurrencyType] = mapped_column(
        Enum(CurrencyType),
        nullable=False
    )
    user_id:Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False
    )
    user:Mapped["User"] = relationship(back_populates="accounts")
    created_at:Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text('now()')
    )

class Category(Base):
    __tablename__ = "categories"
    id:Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    name:Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    type:Mapped[TransactionType] = mapped_column(
        Enum(TransactionType),
        nullable=False
    )
    user_id:Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id",ondelete="CASCADE"),
        nullable=False
    )

class Transaction(Base):
    __tablename__ = "transactions"
    id:Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4
    )
    amount:Mapped[Decimal] = mapped_column(
        Numeric(10,2),
        nullable=False
    )
    description:Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )
    category_id:Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("categories.id"),
        nullable=False
    )
    account_id:Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("accounts.id"),
        nullable=False
    )
    created_at:Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=text('now()')
    )