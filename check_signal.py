import pygame
from pygame.locals import *

pygame.joystick.init()
try:
   joystick = pygame.joystick.Joystick(0)
   joystick.init()
   print('コントローラーの名前:', joystick.get_name())
   print('ボタン数 :', joystick.get_numbuttons())
except pygame.error:
   print('コントローラーが接続されていません')

pygame.init()

active = True
while active:
   for e in pygame.event.get():
        if e.type == QUIT:
            active = False
        print('|'+str(e))
