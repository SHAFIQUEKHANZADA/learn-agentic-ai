from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class Cart(BaseModel):
    user_input: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, max_length=15, description="Employee Name", examples="Shafique Ur Rehman")
    department: Optional[str] = "General"
    salary: float = Field(..., ge=10000)