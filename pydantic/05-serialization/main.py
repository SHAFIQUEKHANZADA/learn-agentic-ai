from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name="Shafique Ur Rehman",
    email="kzshafique77@gmail.com",
    createdAt= datetime(2024, 3, 15, 3, 5),
    address= Address(
        street="123 something",
        city="New York",
        zip_code="70010"
    ),
    is_active=False,
    tags= ["Premium", "Subscriber"]
)

# Using model_dump
our_user = user.model_dump()
print(our_user)

print("----------------\n")

# Using model_dump_json
user_json = user.model_dump_json()
print(user_json)