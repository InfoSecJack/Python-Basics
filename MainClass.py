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
                print("\n"*50)
                userinput = topics[userinput-1]
                try:
                    i = importlib.import_module(userinput)
                    i.lesson("lesson1")
                except KeyboardInterrupt:
                    print("\n"*50)
                    print("You have quit the current lesson\n")
            else:
                print("Please input a number within 1 and {}".format(len(topics)))
        except ValueError:
            print("\n"*50)
            print("That wasn't a number!\n")
        except KeyboardInterrupt:
            print("\n"*50)
                
            
if __name__ == "__main__":
    main()
