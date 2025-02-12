from datetime import datetime
from typing import List

import httpx
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, constr

app = FastAPI()

posts = []
current_id = 1


class PostCreate(BaseModel):
    korisnik: constr(max_length=20)
    tekst: constr(max_length=280)
    vrijeme: datetime


class Post(PostCreate):
    id: int


class UserCredentials(BaseModel):
    korisnicko_ime: str
    lozinka: str


async def authenticate_user(credentials: UserCredentials):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://authapi:8000/login", json=credentials.model_dump()
            )
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=500, detail=f"Failed to connect to authAPI: {e}"
            )


@app.post("/objava", response_model=Post)
def create_post(post_data: PostCreate):
    global current_id
    new_post = Post(id=current_id, **post_data.model_dump())
    posts.append(new_post.model_dump())
    current_id += 1
    return new_post


@app.get("/objava/{id}", response_model=Post)
def get_post(id: int):
    for post in posts:
        if post["id"] == id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")


@app.post("/korisnici/{korisnik}/objave", response_model=List[Post])
async def get_posts_by_user(
    korisnik: str,
    credentials: UserCredentials,
    auth_result: bool = Depends(authenticate_user),
):
    if not auth_result:
        raise HTTPException(status_code=401, detail="Authentication failed")
    user_posts = [post for post in posts if post["korisnik"] == korisnik]
    return user_posts


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3500)
