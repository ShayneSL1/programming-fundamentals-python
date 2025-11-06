#Control Structures / Control Flow

#If Statements
instanceRunning = "Running"

""" if condition:
    #code to execute if condition is True
elif anotherCondition:
    #code to execute if anotherCondition is True
else:
    #code to execute if all other conditions are False. """

if instanceRunning == "Running":
    print("The EC2 is running.")
elif instanceRunning == "Stopped":
    print("The EC2 is stopped.")
else:
    print("The EC2 is in an unexpected state")
