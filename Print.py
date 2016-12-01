#Variables Tutorial
import sys, time, random
class lesson(object):
    
    def __init__(self, lessonType):
        self.lesson = lesson
        getattr(lesson,lessonType)()
    def lesson1():
        #global userin
        #userin = ""
        def rlsmTyp(sentence):
            for l in sentence:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(random.uniform(0,0.1))

        rlsmTyp(
"""Lesson: Printing
Hello - This is the tutorial on how to print something to the screen!

print("Use this as an example for your print function!")
""")
        print(
"""============================
Use this as an example for your print function!
============================""")

        rlsmTyp(
"""
As you can see, there is a name that calls the function, the function has
an opening and closing brackets, and quotations inside them. Remember this!

Lets start you off the traditional way - \"Hello World!\"

OBJECTIVE == Print \"Hello World!\" to the screen
""")
###############################################################################
        answer = "print(\"Hello World!\")"
        while True:
            userin = input(
"""=========================\n#Now it's your turn - Enter your code below
""")
            userin = userin.replace("'","\"").replace("print (","print(",1)
            if userin == answer:
                break
            else:
                print("\n"*8+"ERROR: yourCode != " + answer)
                if userin.count("\"") != 2:
                    print("You missed a speech mark")
                if "(" not in userin or ")" not in userin:
                    print("You missed a bracket")
                if "Hello World!" not in userin:
                    print(
"""Your text is not correct, check if spelled correctly and it is properly
capitalised""")
###############################################################################
        print(
"""============================
Hello World!
============================""")
                
        rlsmTyp(
"""
Well done!

Sometimes, you'll need to connect two sentences together!

I must ask - what's your first name?
""")
        while True:
            userin = input()
            if len(userin.split()) == 1 and len(userin) == 2:
                break
            else:
                print("Try again")
                
        rlsmTyp("print(\"Hello,\" + " + "\"" + userin + "\")")

        print(
"""============================
Hello,"""+userin+"""
============================""")

