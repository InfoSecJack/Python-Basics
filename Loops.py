#Variables Tutorial
import sys, time, random
class lesson(object):


    def __init__(self, lessonType):
        self.lesson = lesson
        getattr(lesson,lessonType)()
    def lesson1():
        printfunc = "Hello! Welcome to the Loops Tutorial!\n"
        for x in printfunc:
            sys.stdout.write(x)
            sys.stdout.flush()
            time.sleep(random.uniform(0,0.05))
