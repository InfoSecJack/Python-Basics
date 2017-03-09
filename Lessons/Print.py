#Print Tutorial
import sys,time,random,os,linecache
path = os.getcwd()
script = os.path.basename(__file__)[:-3]
txt = path + "\\txt\\" + script + ".txt"
def type(sentence):
    for letter in sentence:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.uniform(0,0.1))
        
def main():
    lst = []
    for x in range(sum(1 for line in open(txt))):
        lst.append(linecache.getline(txt, x))
    print(lst)
    for x in range(len(lst)):
        if lst[x] == "":
            pass
        elif lst[x].startswith("#"):
            print(lst[x][1:], end="")
        else:
            type(lst[x])
            
            
    #nothing = type
    #; = print
    #-> = input

    input("\nPress enter to continue.")
    #type()
###############################################################################

    answer = "print(\"Hello World!\")"
    print(
"""=========================
#Now it's your turn - Enter your code below
""")
    while True:
        userin = input().replace("'","\"").replace("print (","print(",1)
        if userin == answer:
            break
        else:
            print("\n"*8+"ERROR: output != \"Hello World!\"")
            if userin.count("\"") != 2:
                print("You missed a speech mark")

            if "(" not in userin or ")" not in userin:
                print("You missed a bracket")

            if "Hello World!" not in userin:
                print("Your text is not correct, check if spelled correctly, and if there is a exclamation mark")
###############################################################################
    print(
"""
============================
Hello World!
============================""")

    type(
"""
Well done!
Sometimes, you'll need to connect two sentences together!
I must ask - what's your first name?
""")
    name = input("My name is ").capitalize()
    while True:
        if len(name.split()) == 1 and len(name) >= 2:
            break
        else:
            print("Try again")

    type("print(\"Hello, \" + \"{}\")".format(name))

    print(
"""
============================
Hello, {}
============================""".format(name))

    type(
"""
This is called Concatenation.
This is used when you need to output a string that isn't always the same,
for example, when using variables, which you will learn next time. But for
now, try and connect one sentence to an already made one!
OBJECTIVE[1] == Concatenate a string to an already set string
""")
################################################################################
    while True:
        hobby = input("print(\"My name is {} and my favourite hobby is \" + ".format(name)).replace("'","\"").replace("\"\)","")
        if hobby.count("\"") == 2 and len(hobby) >= 3:
            hobby = hobby.strip("\"")
            break
        else:
            print("ERROR")
################################################################################
    type(
"""
So your favourite thing to do is {}, huh? Nice!
Alright - That concludes our Python Printing basics, be sure to check
out the other tutorials! Variables will be the next topic.
Until then!
""".format(hobby))
main()
