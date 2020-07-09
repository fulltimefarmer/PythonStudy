import pymongo

client = pymongo.MongoClient(host='10.92.38.76', port=27017)

db = client.common_order_dev

collection = db.order_aoc_content

results = collection.find()

for result in results:
    print(result)
