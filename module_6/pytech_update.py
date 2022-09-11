from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ijsqqy5.mongodb.net/pytech"
client = MongoClient(url)
db = client["pytech"]

docs = db.students.find({})
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
def first_output():
    for doc in docs:
        fname = doc["first_name"]
        lname = doc["last_name"]
        s_id = doc["_id"]
        print(f"Student ID: {s_id}\nFirst Name: {fname}\nLast Name: {lname}\n")
first_output()


db.students.update_one({"_id":1007},{"$set": {"last_name":"Dahmer"}})

print("-- DISPLAYING STUDENT DOCUMENT 1007")
doc = db.students.find_one({"_id": 1007})

def second_output(doc):
    fname = doc["first_name"]
    lname = doc["last_name"]
    s_id = doc["_id"]
    print(f"Student ID: {s_id}\nFirst Name: {fname}\nLast Name: {lname}\n")
second_output(doc)

input("End of program, press Enter to continue... ")