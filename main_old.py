import time
"""

Jace Blears' & Jack Alston's Python 3 programming
basics tutorial, used for helping schoolmates in
Computer Science for their tasks.

Disclaimer:
No answers for any coursework is in this tutorial,
only explanations about the Python language.

This was made for Python 3.4, 3.5, and 3.6, and
possibly higher versions.

"""

lst = ["Printing","Defining Variables","Strings, Integers and Booleans",
       "Modifiers","Indenting, and If, Elif and Else","While Loops","For Loops"]
dicFunctions = {
    1:"printing",2:"defvars",3:"strintbools",4:"mods"#5:#6:#7:#8:
    } 

def getMain():
    
    for x in range(len(lst)):
        print(str(x+1) + ")",lst[x])
    while True:
        userinput = int(input("Choose an option: "))
        if userinput in range(1,len(lst)):
            func = dicFunctions[userinput]
            getattr(get,func)()
        else:
            print("Please input a between 1 and",len(lst))
        #except:
            #print("U dun fuked up")
    print(lst[userinput - 1])
    
class get:

    def __init__(self):
        ""
    
    def priting():
        print("")

    def defvars():
        print("")

    def strintbools():
        print("")

    def mods():
        print("")
        
getMain()

# import time,sys,random
# def realisticTyping():
#     blah = "This is written slowly\n"
#     for x in blah:
#         sys.stdout.write(x)
#         sys.stdout.flush()
#         #Seems to mimic print()
#         time.sleep(random.uniform(0,0.6))
# ################################
# """
# 
# Jace Blears' & Jack Alston's Python 3 programming
# basics tutorial, used for helping schoolmates in
# Computer Science for their tasks.
# 
# Disclaimer:
# No answers for any coursework is in this tutorial,
# only explanations about the Python language.
# 
# This was made for Python 3.4, 3.5, and 3.6, and
# possibly higher versions.
# 
# """
# 
# lst = [
#     "Printing",
#     "Defining Variables",
#     "Strings, Integers and Booleans",
#     "Modifiers",
#     "Indenting, and If, Elif and Else",
#     "While Loops",
#     "For Loops"]
# 
# dicFunctions = {
#     1:"printing",
#     2:"defvars",
#     3:"strintbools",
#     4:"mods",
#     5:"indentifelse"
#     #6:
#     #7:
#     #8:
#     } 
# 
# def getMain():
#     
#     for x in range(len(lst)):
#         print(str(x+1) + ")",lst[x])
#     while True:
#         userinput = int(input("Choose an option: "))
#         if userinput in range(1,len(lst)):
#             func = dicFunctions[userinput]
#             getattr(get,func)()
#         else:
#             print("Please input a between 1 and",len(lst))
#     print(lst[userinput-1])
#     
# class get():
# 
#     #def __init__(self):
#         #""
#     
#     def printing():
#         print("i78907")
# 
#     def defvars():
#         print("")
# 
#     def strintbools():
#         print("")
# 
#     def mods():
#         print("")
#         
# getMain()
#  */

