from pydantic import BaseModel, Field, field_validator, model_validator, computed_field

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be atleast 4 characters")
        return v
    

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password do not match')
        return values
    

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    

# Task 
class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night