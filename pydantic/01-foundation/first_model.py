from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {'id': 101, 'name': "Shafique Ur Rehman", 'is_active': True}

user = User(**input_data)
print(user)


class Product(BaseModel):
    id: int
    name: str
    price: int
    is_stock: bool 

product_input = {"id": 10, "name": "Shirt", "price": 500, "is_stock": "True"}

product = Product(**product_input)
print(product)