import os
from datetime import datetime, timezone
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv(override=True)


def getDataByCurrentDate():
    client = MongoClient(os.environ.get('MONGO_URL'))
    print("test", os.environ.get('MONGO_URL'))
    result = client['sandbox']['templates'].find_one(
        filter={"announced_at": {'$lte': datetime.now(tz=timezone.utc)}}
    )

    return result
