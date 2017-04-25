from pymongo import MongoClient

client = MongoClient(host="localhost")
db = client['sample']
coll = db['sample_coll']
query = {
    "name": "Kishore"

}
records = coll.find(query)

for rec in records:
    print(rec)
coll.update_one(
    {"_id": "58e7d4bfea8f180375c6e407"},
    {set: {
        'is_expired': True
    }
    })
