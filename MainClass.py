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

def main():
    while True:
        print ("Topics: ")
        for x in range(len(topics)):
            print(str(x+1) + ") " + topics[x])
        try:
            userinput = int(input("Pick a topic number: "))
            if userinput in range(1,len(topics)+1):
                print("\n"*39)
                userinput = topics[userinput-1]
                try:
                    i = importlib.import_module(userinput)
                    i.lesson("lesson1")
                except KeyboardInterrupt:
                    print("\n"*39)
                    print("You have quit the current lesson")
                    print("\n")
            else:
                print("Please input a number within 1 and {}".format(len(topics)))
        except ValueError:
            print("That wasn't a number!")
            print("\n"*39)
            
if __name__ == "__main__":
    main()
