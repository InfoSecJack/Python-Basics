#Variables Tutorial
import sys, time, random
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
"""Lesson: Printing

Hello - This is the tutorial on how to print something to the screen!

print("Use this as an example for your print function!")
""")
        print(
"""=========================
Use this as an example for your print function!
============================""")

        rlsmTyp(
"""
As you can see, there is a name that calls the function, the function has
an opening and closing brackets, and quotations inside them. Remember this!

Lets start you off the traditional way - \"Hello World!\"

OBJECTIVE == Print \"Hello World!\" to the screen
""")
        answer = "print(\"Hello World!\")"
        while True:
            tutIn = input(
"""=========================\n#Now it's your turn - Enter your code below
""")
            if tutIn.startswith("print("):
                pass
            else:
                tutIn = tutIn.replace("print (","print(",1)
            if tutIn == answer:
                break
            else:
                print("ERROR: yourCode !=",answer)
