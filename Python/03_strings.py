#strings are immutable in python

name="Ayush Srivastava"

#They are kind of stored in array so if we want to access char at particular index then we can also do it 

index2=name[2]

print(index2)

#python also allow us to generate sub-string as well it will need to index 1st Starting(it is included) 2nd Ending(it is excluded) i.e name[0:5] it will give string from 0 index to 4 index

subString=name[0:5]
print(subString)

#since string are immutable we cann't directly update it's value at any index

# name[0]="a"


firstName="Ayush"
lastName="Srivastava"

# cancatenation of strings 

addition_of_name=firstName+lastName

print(addition_of_name)

# but we can not add strings with number 

text="Total state in India is : "
number_of_states=29
# This will give us error..  can only concatenate str (not "int") to str
# print(text+number_of_states)

# So we need to convert string into number

number_to_string_conversion=str(number_of_states)

print(text+number_to_string_conversion)