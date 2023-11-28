import pygame
from pygame.locals import *
import time

#ボタン
Button_A=0
Button_B=1
Button_X=2
Button_Y=3
#オプション
Button_MINUS=4
Button_HOME=5
Button_PLUS=6

#スティック押し込み
Push_Button_Left=7
Push_Button_Right=8

#トリガー
Button_L=9
Button_R=10

#十字キー
Button_Up=11
Button_Down=12
Button_Left=13
Button_Right=14

Button_CAPTURE=15

#スティック
Axis_Left_Motion_X = 0  # 左スティックの水平方向
Axis_Left_Motion_Y = 1  # 左スティックの垂直方向
Axis_Right_Motion_X = 2  # 右スティックの水平方向
Axis_Right_Motion_Y = 3  # 右スティックの垂直方向

#ZLとZR
Axis_ZL=4
Axis_ZR=5

def main():
    pygame.init()
    pygame.joystick.init()
    joys = pygame.joystick.Joystick(0)
    joys.init()

    count_num=0
    start_time = time.time()  
    run_time = 10  

    print("---------------------Start---------------------")

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= run_time:
            print("----------------------End----------------------")
            print(count_num)
            break  

        # コントローラーの操作を取得
        eventlist = pygame.event.get()
        for e in eventlist:
            if e.type == pygame.locals.JOYBUTTONDOWN:
                count_num+=1
                if e.button == Button_B:
                    print("B down")
                elif e.button == Button_A:
                    print("A down")
                elif e.button == Button_Y:
                    print("Y down")
                elif e.button == Button_X:
                    print("X down")
                elif e.button == Button_MINUS:
                    print("MINUS down")
                elif e.button == Button_HOME:
                    print("HOME down")
                elif e.button == Button_PLUS:
                    print("PLUS down")
                elif e.button == Push_Button_Left:
                    print("Push Left down")
                elif e.button == Push_Button_Right:
                    print("Push Right down")
                elif e.button == Button_L:
                    print("L down")
                elif e.button == Button_R:
                    print("R down")
                elif e.button == Button_Up:
                    print("Up down")
                elif e.button == Button_Down:
                    print("Down down")
                elif e.button == Button_Left:
                    print("Left down")
                elif e.button == Button_Right:
                    print("Right down")
                elif e.button == Button_CAPTURE:
                    print("CAPTURE down")

            elif e.type == pygame.locals.JOYBUTTONUP:
                if e.button == Button_B:
                    print("B up")
                elif e.button == Button_A:
                    print("A up")
                elif e.button == Button_Y:
                    print("Y up")
                elif e.button == Button_X:
                    print("X up")
                elif e.button == Button_MINUS:
                    print("MINUS up")
                elif e.button == Button_HOME:
                    print("HOME up")
                elif e.button == Button_PLUS:
                    print("PLUS up")
                elif e.button == Push_Button_Left:
                    print("Push Left up")
                elif e.button == Push_Button_Right:
                    print("Push Right up")
                elif e.button == Button_L:
                    print("L up")
                elif e.button == Button_R:
                    print("R up")
                elif e.button == Button_Up:
                    print("Up up")
                elif e.button == Button_Down:
                    print("Down up")
                elif e.button == Button_Left:
                    print("Left up")
                elif e.button == Button_Right:
                    print("Right up")
                elif e.button == Button_CAPTURE:
                    print("CAPTURE up")
            elif e.type == pygame.locals.JOYAXISMOTION:
                if e.axis == Axis_Left_Motion_X:
                    print("LEFT STICK ACTIVE")
                elif e.axis == Axis_Left_Motion_Y:
                    print("LEFT STICK ACTIVE")
                elif e.axis == Axis_Right_Motion_X:
                    print("RIGHT STICK ACTIVE", e.value)
                elif e.axis == Axis_Right_Motion_Y:
                    print("RIGHT STICK ACTIVE")
                elif e.axis == Axis_ZL:
                    print("ZL ACTIVE")
                elif e.axis == Axis_ZR:
                    print("ZR ACTIVE")
            

if __name__ == "__main__":
    if input("Enter Key --> 開始")=="":
        main()
