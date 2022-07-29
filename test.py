import pymongo

'''pip install pymongo'''

client = pymongo.MongoClient("mongodb+srv://Mickey0195:Maa2365@@mickey.xtekati.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)