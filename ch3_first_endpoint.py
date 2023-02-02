from enum import Enum
from fastapi import Body, FastAPI, File, Form, Path, Query, UploadFile, status
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


class Company(BaseModel):
    name: str


app = FastAPI()


class UserTypes(str, Enum):
    admin = "admin"
    standard = "standard"


class UsersFormat(str, Enum):
    SHORT = "short"
    FULL = "full"


@app.get("/users/{id}")
async def get_user(id: int = Path(..., ge=1)):
    return {"id": id}


@app.get("/licenses/{license}")
async def get_license(license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")):
    return {"license": license}


@app.get("/users")
async def get_users(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
    return {"page": page, "size": size}


@app.get("/userformat")
async def get_user(format: UsersFormat = UsersFormat.SHORT):
    return {"format": format}


@app.post("/users")
async def create_user(user: User):
    return {"name": user.name, "age": user.age}


@app.post("/usersComplex")
async def create_user(user: User, company: Company):
    return {"name": user.name, "age": user.age, "company": company.name}


@app.post("/usersForm")
async def create_user(name: str = Form(...), age: int = Form(...)):
    return {"name": name, "age": age}


@app.post("/files")
async def create_file(file: UploadFile = File(...)):
    return {"file_content_type": file.content_type, "file_name": file.filename}


class Post(BaseModel):
    title: str


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    return post
