from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_DB_URI = MONGO_DB_URI = os.getenv('MONGO_DB_URI')

client = MongoClient(MONGO_DB_URI)

db = client.cv_db

collection_name = db['cv_collection']
