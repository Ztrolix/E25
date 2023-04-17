#setup
from time import sleep
import random
import time
import os
import datetime
import turtle
import tkinter
from tkinter import *
import math

print(r"""  ______   ___    _____ 
 |  ____| |__ \  | ____|
 | |__       ) | | |__  
 |  __|     / /  |___ \ 
 | |____   / /_   ___) |
 |______| |____| |____/ 
                        
                        """)
print("E25 [ Version 1.0.0a1 ]")
print("(c) E25. All rights reserved.")
print()

while True :
    a = str(input(": "))
    if (a == "bazt") :
      print("bazt [ Version 1.0.0 ]")
    else :
      if "bazt install " in a :
        print("ERROR: Could not find a version that satisfies the requirement " + str(a) + " (from versions: none)")
      else:
        print(r"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '""" + str(a) + "' is not defined")