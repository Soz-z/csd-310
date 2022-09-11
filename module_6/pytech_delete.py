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

print("-- INSERT STATEMENTS --")
def create_student(fname,lname,id=int):
    student = {
        "_id":id,
        "first_name":fname,
        "last_name":lname
    }
    new_student_id = db.students.insert_one(student).inserted_id
    print(f"Inserted student record into the students collection with document_id", new_student_id)

create_student("Jimmy","Jusco",1010)
print("\n")

print("-- DISPLAYING STUDENT TEST DOC --")

query_one = db.students.find_one({"_id": 1010})
def query_find_one(doc):
    fname = doc["first_name"]
    lname = doc["last_name"]
    s_id = doc["_id"]
    print(f"Student ID: {s_id}\nFirst Name: {fname}\nLast Name: {lname}\n")
query_find_one(query_one)

# DELETE THE STUDENT HERE
db.students.delete_one({"_id":1010})
# FIND() QUERY
docs = db.students.find({})
print(" -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

def find_all():
    for doc in docs:
        fname = doc["first_name"]
        lname = doc["last_name"]
        s_id = doc["_id"]
        print(f"Student ID: {s_id}\nFirst Name: {fname}\nLast Name: {lname}\n")
find_all()