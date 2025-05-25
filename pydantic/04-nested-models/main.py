from typing import List, Dict, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code = str


class User(BaseModel):
    id: int
    name: str
    address: Address

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None

Comment.model_rebuild()


address = Address(
    street="123 something",
    city="New york",
    postal_code="1234"
)

user = User(
    id=1,
    name="Shafique Ur Rehman",
    address=address
)

comment = Comment(
    id=1,
    content="Nice Photo",
    replies= [
        Comment(id=2, replies="Thank You")
    ]
)