import pymongo

#creating connectivity
client = pymongo.MongoClient("mongodb+srv://bhkris:bhkris@bhar-cluster.bfpna.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client["myinfo"]
collection = database["bhar_coll"]


data = collection.find({"company_name" : "iNeuron"})
data = collection.find({})
for i in data:
    print(i)