from pydantic import BaseModel, Field, root_validator
from typing import List

class Product(BaseModel):
    id: int
    name: str
    price: float

class Order(BaseModel):
    order_id: int
    user_id: int = Field(..., alias="userID")
    products: List[Product]
    total_amount: float = 0.0

    @root_validator
    def calculate_total(cls, values):
        products = values.get('products', [])
        values['total_amount'] = sum(p.price for p in products)
        return values

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

# Usage
order_data = {
    "order_id": 1001,
    "userID": 10,
    "products": [
        {"id": 1, "name": "Pen", "price": 20.0},
        {"id": 2, "name": "Notebook", "price": 50.0}
    ]
}

order = Order(**order_data)
print(order)
