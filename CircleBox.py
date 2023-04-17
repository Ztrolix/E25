import pygame
import sys
import random
import time
import os
import logging
import datetime
from pygame import mixer
from pathlib import Path
from pygame.locals import *
import urllib.request
import urllib.error
import turtle
import tkinter
from tkinter import ttk
import math
from time import sleep
from tqdm import tqdm
from tqdm import tqdm_gui

file = Path()
e = datetime.datetime.now()
print (e.strftime("%Y-%m-%d %H:%M:%S"))
print (e.strftime("%d/%m/%Y"))
print (e.strftime("%I:%M:%S %p"))
print (e.strftime("%a, %b %d, %Y"))
path_to_file2 = (e.strftime("%Y-%m-%d-%H-%M-%S.txt"))
path2 = Path(path_to_file2)
filePath = "assets\\logs\\" + path_to_file2
file = open(filePath,"w")
L = ["-------------------\n","     Circle Box\n","-------------------\n"," \n","Game Started ",e.strftime("%Y-%m-%d %H:%M:%S"),"\n"]
file.writelines(L)
file.close()
logging.basicConfig(filename=filePath, level=logging.DEBUG)
logging.debug("Debug logging test...")
file = open(filePath,"a")
LA = ["Log file started!\n"]
file.writelines(LA)
file.close()

d = 0
turtle.title("Circle Box Launcher")
#for d in tqdm(range(random.randint(5, 20))):
#    sleep(random.randint(1, 5))
img = tkinter.Image("photo", file="CircleBox3.png")
turtle._Screen._root.iconphoto(True, img)
sc = turtle.Screen()
sc.setup(400,300)
turtle.setx(-200)
turtle.setx(0)
turtle.forward(400)
turtle.Screen().bgcolor("black")
pygame.init() 
win = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Circle Box")
icon = pygame.image.load('CircleBox3.png')
pygame.display.set_icon(icon)
color = (33, 166, 196)
win.fill(color)
file = open(filePath,"a")
LA = ["Window Loaded\n"]
file.writelines(LA)
file.close()

width = 0
i = 0
bg_img = pygame.image.load("assets\\maps\\load.png")

path_to_file = 'ZtrolixLib\ZtrolixLib.py'
path = Path(path_to_file)
file = open(filePath,"a")
LA = ["ZtrolixLib Found\n"]
file.writelines(LA)
file.close()
if path.is_file():
    f = open('ZtrolixLib\ZtrolixLib.py', 'r')
    content = f.read()
    print("ZtrolixLib Found")
else:
    print("Sorry but the ZtrolixLib is not installed!")
    pp = input("Click any to close.")
    pygame.quit()

modLoca1 = 'ModHandler\modhandler.py'
modLoca1path = Path(modLoca1)
file = open(modLoca1,"a")
ML1 = ["Mod Found\n"]
file.writelines(LA)
file.close()
if path.is_file():
    f = open('ModHandler\modhandler.py', 'r')
    content = f.read()
    print("Mod Handler Found")
else:
    print("Sorry but the ModHandler is not installed!")
    pp = input("Click any to close.")
    pygame.quit()

def gameQuit():
    print("Closing Game")
    run = False
    file = open(filePath,"a")
    LA = ["Game Closed\n"]
    file.writelines(LA)
    file.close()
    pygame.quit()
    sys.exit()

LoadPer = 0
GameStart = 0
GLoadPer = 0

run = True
while run:
    keys = pygame.key.get_pressed()

    win.fill((0,0,0))
    win.blit(bg_img,(i,0))
    win.blit(bg_img,(width+i,0))
    if (i==-width):
        win.blit(bg_img,(width+i,0))
        i=0
    i-=0

    if (LoadPer >= 100) :
        print("LoadedGame")
        print("Found Lobby")
        bg_img = pygame.image.load("assets\\maps\\Menu.png")
        LoadPer = -1
        GameStart = 1
    else :
        if not(LoadPer <= -1) :
            LoadPer = LoadPer + 1
            print(int(LoadPer))

    if (GameStart == 1) :
        if (GLoadPer >= 100) :
            
            print("You Are Now In A lobby")
            print("1 / 10 Players In Lobby")
            bg_img = pygame.image.load("assets\\maps\\Game1.png")
            os.system('CircleBox.exe')
            GLoadPer = -1
        else :
            if not(GLoadPer <= -1) :
                GLoadPer = GLoadPer + 2
                print(int(GLoadPer))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameQuit()

    pygame.display.update() 
