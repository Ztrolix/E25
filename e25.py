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
from tqdm import tqdm
from tqdm import tqdm_gui
import requests

ztrolibins = 'https://github.com/Ztrolix/ZtrolixLib.git'
ztrolibinsr = requests.get(ztrolibins, allow_redirects=True)



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
        if (a == "bazt install ztrolib") :
          print("Found Ztrolib.")
          print("Downloading...")
          for i in tqdm(range(random.randint(10, 100))):
           ...
           sleep(random.randint(0, 2))
          print("Installing...")
          open('facebook.ico', 'wb').write(ztrolibinsr.content)
          for i in tqdm(range(random.randint(10, 100))):
           ...
           sleep(random.randint(0, 2))
          print("Successfully installed!")
        else :
          print("ERROR: Could not find a version that satisfies the requirement '" + str(a) + "' (from versions: none)")
      else:
        print(r"""Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name '""" + str(a) + "' is not defined")