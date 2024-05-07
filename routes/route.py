from fastapi import APIRouter
from models.skills import Skill
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# get request method


@router.get('/')
async def get_skills():
    skills = list_serial(collection_name.find())
    return skills

# post requiest


@router.post('/')
async def post_skill(skill: Skill):
    collection_name.insert_one(dict(skill))

# put requiest


@router.put("/{id}")
async def put_skill(id: str, skill: Skill):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(skill)})


# delete requiest
@router.delete("/{id}")
async def delete_skill(id: str):
    collection_name.delete_one(
        {"_id": ObjectId(id)})
