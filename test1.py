import pymongo

''' pip install "pymongo[srv]  '''
client = pymongo.MongoClient("mongodb+srv://mayank:Maa2365@cluster0.ln5hbfz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    'name':'mayank',
     'email':'mayankghai1195@gmail.com',
     'surname':'ghai'

}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)