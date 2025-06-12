from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional

class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=3)
    email: EmailStr
    age: Optional[int] = None
    address: Address

    @validator('age')
    def age_must_be_positive(cls, value):
        if value is not None and value <= 0:
            raise ValueError('Age must be positive')
        return value

# Usage
user = User(
    id=1,
    name='Ted Mosby',
    email='tedmosby@gmail.com',
    age=35,
    address={'city': 'New York', 'pincode': 400001}
)
print(user)
