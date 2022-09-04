from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ijsqqy5.mongodb.net/pytech"
client = MongoClient("mongodb+srv://admin:admin@cluster0.ijsqqy5.mongodb.net/pytech")
db = client.pytech


print("-- Python Collection List --")
print(db.list_collection_names())
print("\n")
input("End of program, press any key to exit... ")
