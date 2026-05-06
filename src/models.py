from sqlalchemy import String
from sqlalchemy.orm import declarative_base, Mapped, mapped_column


Base = declarative_base()


class Subscriber(Base):
    __tablename__ = "subscribers"

    id:             Mapped[int]     = mapped_column(primary_key=True)
    email:          Mapped[str]     = mapped_column(unique=True, nullable=False)
    phone_number:   Mapped[str]     = mapped_column(unique=True, nullable=False)

    def __repr__(self):
        return f"\nSubscriber ID: {self.id}\nEmail: {self.email}\nPhone Number: {self.phone_number}\n"
    