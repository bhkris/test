import pymongo

#creating connectivity
client = pymongo.MongoClient("mongodb+srv://bhkris:bhkris@bhar-cluster.bfpna.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]


database = client["inventory"]
collection = database["table"]
#collection.insert_many(data)

# select operations (retrieve and show all the data in the o/p)
# d = collection.find()
# for i in d:
#     print(i)

#select operation - retrieve based on where filter cond
# d = collection.find({"status": "A"})
# d = collection.find({"status": {'$in':['A','P']}})  #status is in('A','P')
# d = collection.find({'qty':{'$gte':100}}) # >= 100
# d = collection.find({'status':{'$gt':'C'}}) # >C
# d = collection.find({'item':'sketch pad' , 'qty':95})
# d = collection.find({'item':'sketch pad' , 'qty':{'$gte':75}}) # where cond - and
# d = collection.find({'$or': [{'item':'sketch pad'},{'qty':{'$gte':75}}]})  # wwhere cond - or
#updating the record
collection.update_one({'item':'canvas'},{'$set':{'item':'new_canvas'}})

d = collection.find({'item':'new_canvas'})
for i in d:
    print(i)


