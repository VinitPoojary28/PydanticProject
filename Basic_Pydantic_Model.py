from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    email: str
    location: str
    gender: str

user = UserProfile(name="Vinit", age=21, email="vinitpoojary28@gmil.com", location="Mumbai", gender="Male")
print(user.dict())