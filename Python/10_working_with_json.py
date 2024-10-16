#JSON(JavaScript Object Notation)

directory={}


directory["Amit Sharma"] = {
    "address": "1234 MG Road, Delhi, India",
    "phone": "+91-9876543210"
}

directory["Neha Gupta"] = {
    "address": "56 Park Street, Kolkata, India",
    "phone": "+91-8765432109"
}

directory["Rajesh Kumar"] = {
    "address": "78 Central Avenue, Mumbai, India",
    "phone": "+91-9123456780"
}
directory["Ayush Srivastava"] = {
    "address": "Mgs Field, Uttar Pradesh, India",
    "phone": "+91-9138483937"
}

import json

jsonString=json.dumps(directory)
#it will dump the directory in form string and covert it into json object

# print(jsonString)

# it will help to write the string into a file in form of json or text
# w means we are writing the file

with open("C://Users//Admin//Desktop//ML-Journey//Python//directory.json", "w") as f:
    f.write(jsonString)
with open("C://Users//Admin//Desktop//ML-Journey//Python//directory.txt", "w") as f:
    f.write(jsonString)

# to read the file
#  r refers to reading which means we are reading the file

f=open("C://Users//Admin//Desktop//ML-Journey//Python//directory.txt", "r")
readData=f.read()
print(readData)
print("type of readData = "+" " + str(type(readData)))