from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ijsqqy5.mongodb.net/pytech"
client = MongoClient("mongodb+srv://admin:admin@cluster0.ijsqqy5.mongodb.net/pytech")
db = client.pytech
print("-- INSERT STATEMENTS --")
def create_student(fname,lname,id=int):
    student = {
        "_id":id,
        "first_name":fname,
        "last_name":lname
    }
    new_student_id = db.students.insert_one(student).inserted_id
    print(f"Inserted student record {fname} {lname} into the students collection with document_id", new_student_id)

create_student("Fred","Jackson",1007)
create_student("Dan", "Smith", 1008)
create_student("James", "John", 1009)



print("\n")

input("End of program, press enter to exit... ")

