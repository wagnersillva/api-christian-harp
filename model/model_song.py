from pydantic import BaseModel
from typing import Optional

class Song(BaseModel):
    number: int
    author: Optional[str] = None
    title: Optional[str] = None
    text: str