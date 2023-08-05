import sys
import inspect
import zipfile
import os
import fnmatch

def debug(switch, *args):
    if switch:
        callerframe = inspect.getouterframes(inspect.currentframe())[1]
        line, caller = callerframe[2], callerframe[3]
        context = "%s:%d" % (caller, line)
        print("%-20s:" % (context), " ".join(map(str, args)))
        
        
        
def nopfn(*args):
    pass


