from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base


class Beta(Base):
    __tablename__ = "bets"

    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[str] = mapped_column(nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(default='pending')
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())


