#Variables Tutorial
import sys,time,random
class lesson(object):

    def __init__(self, lessonType):
        self.lesson = lesson
        getattr(lesson,lessonType)()
    def lesson1():
        def rlsmTyp(sentence):
            for l in sentence:
                sys.stdout.write(l)
                sys.stdout.flush()
                time.sleep(random.uniform(0,0.1))

        rlsmTyp(
"""
|================|
|Lesson: Printing|
|================|

Hello - This is the tutorial on how to print something to the screen!

print("Use this as an example for your print function!")
""")
        print(
"""
============================
Use this as an example for your print function!
============================""")

        input("\nPress enter to continue.")
        rlsmTyp(
"""
As you can see, there is a name that calls the function, the function has
an opening and closing brackets, and quotations inside them. Remember this!

Lets start you off the traditional way - \"Hello World!\"

OBJECTIVE[0] == Print \"Hello World!\" to the screen
""")
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

        rlsmTyp(
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

        rlsmTyp("print(\"Hello, \" + \"{}\")".format(name))

        print(
"""
============================
Hello, {}
============================""".format(name))

        rlsmTyp(
"""
This is called Concatenation.

This is used when you need to output a string that isn't always the same,
for example, when using variables, which you will learn next time. But for
now, try and connect one sentence to an already made one!

OBJECTIVE[1] == Concatenate a string to an already set string
""")
################################################################################
        while True:
            hobby = input("print(\"My name is {} and my favourite hobby is \" + ".format(name)).replace("'","\"")
            if hobby.count("\"") == 2 and len(hobby) >= 3:
                hobby = hobby.strip("\"")
                break
            else:
                print("ERROR")
################################################################################
        rlsmTyp(
"""
So your favourite thing to do is {}, huh? Nice!

Alright - That concludes our Python Printing basics, be sure to check
out the other tutorials! Variables will be the next topic.

Until then!
""".format(hobby))
