from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

def database_request():
    client = MongoClient(os.getenv("MONGODB_URL"))

    db = client["reviews"]
    my_collection = db["issues"]

    document = my_collection.find()

    return document.to_list()[-1].get("description","UNKNOWN")

if __name__ == "__main__":
    print(database_request())