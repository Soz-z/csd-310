from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ijsqqy5.mongodb.net/pytech"
client = MongoClient("mongodb+srv://admin:admin@cluster0.ijsqqy5.mongodb.net/pytech")
db = client.pytech

docs = db.students.find({})
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

def first_output():
    for doc in docs:
        fname = doc["first_name"]
        lname = doc["last_name"]
        s_id = doc["_id"]
        print(f"Student ID: {s_id}\nFirst Name: {fname}\nLast Name: {lname}\n")
first_output()

print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY--")
doc = db.students.find_one({"_id": 1007})

def second_output(doc):
    fname = doc["first_name"]
    lname = doc["last_name"]
    s_id = doc["_id"]
    print(f"Student ID: {s_id}\nFirst Name: {fname}\nLast Name: {lname}\n")
second_output(doc)

input("End of program, press Enter to continue... ")

# Still unsure on how to code a "press any key to exit...", I know I can make one if the platform is always Windows.