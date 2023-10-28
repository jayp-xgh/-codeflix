from datetime import datetime 
from dataclasses import dataclass, field
from typing import Optional
@dataclass()
class Category:
    name: str
    description: Optional[str] = None
    is_active: Optional[bool] = True
    create_at: Optional[datetime] = field(default_factory=lambda: datetime.now)
