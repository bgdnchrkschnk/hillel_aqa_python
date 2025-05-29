from pydantic import BaseModel

class UserPost(BaseModel):
    id: int
    user_id: int
    title: str
    body: str