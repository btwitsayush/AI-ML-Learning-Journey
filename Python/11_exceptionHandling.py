# Whenever a error occur the program terminates .
# But if we want our code to still work fine even after any exception then we can use exception handling


firstNumber=input("Enter the first Number: ")
firstNumber=int(firstNumber)
secondNumber=input("Enter the second Number: ")
# secondNumber=int(secondNumber)


# try block (in this block we write those code where we think error can occur)

try:
    z=firstNumber/secondNumber
except Exception as e: #it will handle the exception
    print("The exception which occured is :"+ str(e))
    print("Name of exception is ",type(e).__name__) #to get the exact name of exception
    z="Something went wrong" 
finally:
    print(z)
    print("Code Exection done !!")