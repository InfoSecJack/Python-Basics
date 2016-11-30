import importlib

topics = [
    "Print",
    "Variables",
    "Input",
    "Loops"]


for x in range(len(topics)):
    print (str(x+1) + ") " + topics[x])
userinput = int(input("Pick a topic number: "))
userinput = topics[userinput -1]
i=importlib.import_module(userinput)
i.lesson("lesson1")
input("")
