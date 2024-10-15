#There are mainly  types of loop for,while,do-while but we will mainly use 2 of them for and while

# In loop we frequently use 2 keywords
# 1)break -> To break the loop when certain condtion meet
# 2)continue -> To skip a particular condition


# Use case 1 create a program to find sq of even numbers only but except 4 

'''
firstNumber=input("Enter the start of range")
firstNumber=int(firstNumber)

secondNumber=input("Enter the end of range")
secondNumber=int(secondNumber)

for i in range(firstNumber,secondNumber+1):

    if(i==4):
        continue
    if(i%2==0):
        print(i*i)
'''




# Use case -2 given a list of item price find total of it

'''
# using for-each loop

itemsPrice=[100,345,88778,566,9786]

totalPrice=0

for item in itemsPrice:
    totalPrice+=item


print(totalPrice)

'''

# We can also do the above question using for loop

itemsPrice=[100,345,88778,566,9786]

totalPrice=0

for items in range(len(itemsPrice)):
    totalPrice+=itemsPrice[items]

print(totalPrice)

    

# While loop

# Use case-3 
# Run a while loop till 5 increment it by 1 and when value ==3 break;


i=0
while(i<=5):
    if(i==3):
        print("i value is 3 so break the loop")
        break
    else:
        print("i value is not 3 right-now")
    i+=1