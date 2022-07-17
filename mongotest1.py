import pymongo
#creating connection between pycharm and cloud DB (mongo)
client = pymongo.MongoClient("mongodb+srv://bhkris:bhkris@bhar-cluster.bfpna.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "bhar",
    "email" : "bhar@gmail.com",
    "surname" : "k"
}

db_var1 = client['mongotest']
coll = db_var1['test']
coll.insert_one(d )