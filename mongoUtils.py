import os
from datetime import datetime, timezone
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

async def getDataByCurrentDate():
    client = MongoClient(os.getenv('MONGO_URL'))

    result = client['sandbox']['templates'].find_one(
        filter={"announced_at": {'$lte': datetime.now(tz=timezone.utc)}}
    )

    return result
