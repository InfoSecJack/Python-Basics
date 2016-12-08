import importlib

topics = [
    "Print",
    "Variables",
    "Inputs",
    "If Statements and Indentation",
    "While and For loops"]

#advancedTopics = [
    #"Formatting",
    #"Functions"]
lentopic = len(topics)
hide = 37 - lentopic

def main():
    for x in range(lentopic):
        print(str(x+1) + ") " + topics[x])
    try:
        while True:
            userinput = int(input("Pick a topic number: "))
            if userinput in range(1,len(topics)):
                print("\n"*39)
                userinput = topics[userinput-1]
            else:
                print("Please input a number within 1 and {}".format(lentopic))
            i = importlib.import_module(userinput)
            i.lesson("lesson1")
            
    except KeyboardInterrupt:
        print("You have quit the lesson")
        print("\n"*hide)
        
if __name__ == "__main__":
    main()
