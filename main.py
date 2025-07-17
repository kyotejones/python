intCalToUnits = 24
strNameOfUnits = "hours"

def daysToUnits(intNumDays):
    return f"{intNumDays} days are {intNumDays * intCalToUnits} {strNameOfUnits}"

def validateAndExec():
    try:

        intUserInput = int(strUserInput)
        if intUserInput > 0:
            strCalValue = daysToUnits(intUserInput)
            print(strCalValue)
        elif intUserInput == 0:
            print("Please provide a value greater than zero.")

    except ValueError:
        print("Your input is not a valid whole number. Dont ruin my program.")

strUserInput = input("Hey User, enter a number of days and I will convert it to hours\n")

validateAndExec()