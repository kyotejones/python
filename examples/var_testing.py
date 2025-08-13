### Data Types
intAge = 10                 # Integer
floCost = 10.10             # Float
strName = "Demeron Jones"   # String
bolTrueFalse = True         # boolean
print(type(intAge))
print(type(floCost))
print(type(strName))
print(type(bolTrueFalse))

### String Concatenation
print("20 days are " + str(20 * 24 * 60) + " minutes")
print(f"20 days are {20 * 24 * 60} minutes") # only works with newer Python versions. "f" means format

### Variables
intCalulateMinutes = 24 * 60
strUnitOfMeasurement = "minutes"
print(f"20 days are {20 * intCalulateMinutes} {strUnitOfMeasurement}") # 20 days
print(f"30 days are {30 * intCalulateMinutes} {strUnitOfMeasurement}") # 30 days
print(f"365 days are {365 * intCalulateMinutes} {strUnitOfMeasurement}") # 365 days


### Functions & Input Parameters
def daysToUnits(intDays, strMessage):
    print(f"{str(intDays)} days are {intDays * intCalulateMinutes} {strUnitOfMeasurement}")
    print(strMessage)

daysToUnits(10, "Awesome!") # calling the function we created
daysToUnits(365, "Good To Go.") # calling the function we created
# Functions should have two spaced before and after
# Functions should have two spaced before and after
### Variable Scope
def scopeFuncTest(intNumber):
    strTestScope="Testing" # This variable cannot be seen outside this function. Scope is limited.
    print(f"{strTestScope} {intNumber}")
# Functions should have two spaced before and after
# Functions should have two spaced before and after
scopeFuncTest(20)


### User Input
strYourName = input("Hello, what is your name?\n")
print(f"Hello {strYourName}.")


### Function & Return Values
def calculateChange(floCost, floMoneyRecieved):
    floChange = floMoneyRecieved - floCost
    return floChange

floChange = calculateChange(9.99, 20)
print(f"Here is your change: ${floChange}")


### Casting
strDays = input("How many days would you like to see in hours?\n") # User input is always a string
daysToUnits(int(strDays), f"This is {strDays} Days.") # We have to change strDays from a string to an integer (casting).


### Conditionals
intNumber01 = input("Give me a number.\n")
print(intNumber01.isdigit())
if int(intNumber01) > 10:
    print(f"{intNumber01} is greater than 10")
elif int(intNumber01) == 0:
    print("you entered a 0")
else:
    print("Not greater than 10")


### Exception Handling (Try/Except)
intTryNumber = input("Exception: Give me a number\n")
try:
    if int(intTryNumber) > 0:
        print(f"The number you gave is greater than 0: {intTryNumber}")
    else:
        print(f"The number you gave is less than or equal to 0: {intTryNumber}")
except Exception:
    print("What?! Something broke.")