import importlib

topics = [
    "Print",
    "Variables",
    "Inputs",
    "Loops",
    "test"]
lentopic = len(topics)
hide = 37 - lentopic

while True:
    for x in range(lentopic):
        print(str(x+1) + ") " + topics[x])
    try:
        userinput = int(input("Pick a topic number: "))
        if userinput in range(1,lentopic):
            break
    except:
        print("Please input a number")
        print("\n"*hide)
print("\n"*39)
userinput = topics[userinput-1]
i = importlib.import_module(userinput)
i.lesson("lesson1")
