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
import zipfile

ztrolibins = 'https://github.com/Ztrolix/E25/raw/main/bazt/scripts/temp001.zip'
ztrolibinsr = requests.get(ztrolibins, allow_redirects=True)

testf = open("bazt\\scripts\\test\\test.e25", "r")

print(r"""  ______   ___    _____ 
 |  ____| |__ \  | ____|
 | |__       ) | | |__  
 |  __|     / /  |___ \ 
 | |____   / /_   ___) |
 |______| |____| |____/ 
                        
                        """)
print("E25 [ Version 1.0.0a3 ]")
print("(c) E25. All rights reserved.")
print()

while True :
    a = str(input(": "))
    if (a == "bazt") :
      print("bazt [ Version 1.1.0 ]")
    else :
      if "bazt install " in a :
        if (a == "bazt install ztrolib") :
          print("Found Ztrolib.")
          print("Downloading...")
          for i in tqdm(range(random.randint(10, 100))):
           ...
           sleep(random.randint(0, 2))
          open('bazt\\install\\ztrolib\\ZtroLib.zip', 'wb').write(ztrolibinsr.content)
          print("Unzipping...")
          print("Installing...")
          for i in tqdm(range(random.randint(10, 100))):
           ...
           sleep(random.randint(0, 2))
          print("Successfully Installed!")
        else :
          print("ERROR: Could not find a version that satisfies the requirement '" + str(a) + "' (from versions: none)")
      else:
        if (a == "test.e25") :
          print(testf)
          try :
            for x in testf:
              print(x)
          except :
            print("Error: Read file 'test.e25'.")
        else :
          if (a == "run") :
            print("Please input a '.e25' file.")
            try :
              filerun = str(input("> "))
              runf = open(filerun, "r")
            except :
              print("Error: File '" + str(filerun) + "' has given a error.")
            if ".e25" in filerun :
              for y in runf:
                  print(y)
              while True :
                runask = input("Do you want to run this file? [ Y or N ] ")
                if (runask == "y") :
                  print("Error: File '" + str(filerun) + "' has errors in its code.")
                  break
                else:
                  if (runask == "n") :
                    break
                  else: 
                    print("Error: '" + str(runask) + "' is not a valid input.")
            else :
              print("Error: File '" + str(filerun) + "' is not a '.e25' file.")
          else  :
            # new script here
            print("Error: Name '" + str(a) + "' is not defined")