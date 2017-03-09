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
"""Lesson: Variables

Todo:
Acceptable variables

Variable names cannot BEGIN with a number
Variable1 = Sure, but poorly named
myVar = Yes
my_var = Yes

""")
