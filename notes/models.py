from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Note:
    id: int
    title: str
    text: str
    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )