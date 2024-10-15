# We use conditional statememt to check something on the basis of condition




# Use Case: Scholarship Eligibility Check
# You are building a program that checks if a student is eligible for a scholarship based on their:

# Age.
# GPA.
# Income of the family.
# Whether they are involved in extracurricular activities.
# Conditions:
# If the student's age is between 18 and 25 (inclusive), and they have a GPA of 3.5 or above, and their family income is less than $50,000, print: "Eligible for full scholarship."
# If the student's GPA is above 3.0 or they are involved in extracurricular activities, print: "Eligible for partial scholarship."
# If the student's GPA is less than 2.0, or their age is above 30, print: "Not eligible for any scholarship."
# If the student's family income is above $100,000 and they are not involved in extracurricular activities, print: "Not eligible due to high family income."
# If none of the above conditions are met, print: "Check the student's profile for special cases."


age=input("Enter your age ")
age=int(age)

gpa=input("Enter your gpa ")
gpa=float(gpa)

income=input("Enter income of your family ")
income=int(income)

condition=input("Are you enrolled in extracurricular activities ? Tell in Yes OR No only..")

if(age>=18 and age<=25 and gpa>=3.5 and income<50000):
    print("Eligible for full scholarship.")
elif(gpa>3.0 or condition=="Yes" ):
    print( "Eligible for partial scholarship.")




