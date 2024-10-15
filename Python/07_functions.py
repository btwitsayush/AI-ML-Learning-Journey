
# Function is a block of code that performs a specific task when called 


# Implement a function to sum 2 values


def sumOfNumbers(a=0,b=0): # giving a default value to argyment in case if someone passes only 1 parameter than it will be used
    total=a+b
    return total

firstOutput=sumOfNumbers(5,6)#5 will be assigned to a and 6 will be assigned to b. Bascially it sets value in order
secondOutput=sumOfNumbers(b=8,a=7)# if you don't want to assign values in order than we can also do this way
thirdOutput=sumOfNumbers(8)#8 will be assigned to a . and as we are not passing other parameter it will use by default value


print(firstOutput)
print(secondOutput)
print(thirdOutput)
