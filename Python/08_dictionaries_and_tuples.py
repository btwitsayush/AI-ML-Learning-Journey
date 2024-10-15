
#dictionary allow us to store data in key value pair also k/a HashTables,Map,Associate Array

# Use case -> Create a phone directory and to mainpulation within it 


directory={
    "ayush":6393964912,
    "maroof":763767863,
    "manuj":6787643673
}
# to add a new value 
directory["jennin"]=8887697674

# to access value of particular key

print(directory["ayush"])

# to iterate over a dictonary we can use for loop

for keys in directory:
    print(directory[keys])

# to delete a key
del directory["jennin"]
    
# we can alos do this as well

for k,v in directory.items():
    print("key is " + k + " and its value is " + str(v))

# to clear the directory we can use 

directory.clear()

print(directory)


# tuples  

# tuples and list are kind of similar but with tuples we store different types of value while in list we have to store value of 1 data type . And also tuple are immutable 

address=("vinowapuri near mgs field","Sultanpur",228001)
print(address[0])

address[0]="it will give us error as we can't directly update this"
