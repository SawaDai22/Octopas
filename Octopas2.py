import threading
import time
import tkinter
import random
from datetime import datetime
import requests
import sys

# 初期体力上限
hpMax = 100

# 体力
hp = 50

# 好感度
fp = 0

# なでれる回数
pp = 10

# つつくのあたり回数
hit = 0

# つつける回数
entire = 10

stage = "若年期"

# t1 スレッドが生存しているかを示すフラグ
t1_alive = True

def quit_me(root_window):
    root_window.quit()

# 体力パック
def danger():
    global hp
    global fp
    global t1_alive

    if hp < hpMax:
        f = random.randint(0, 100)

        if f < 20:
            hp -= 10
            print(f"プラスチックを上げました：現在体力{hp}")
            fp -= 10
            if fp < 0:
                fp = 0
                print(f"好感度が10下がった：現在好感度{fp}")
            else:
                print(f"好感度が10下がった：現在好感度{fp}")
            you_died()

        elif f >= 20 and f < 40:
            hp -= 99999
            print(f"デスソースを上げました：現在体力{hp}")
            if fp < 100:
                print(f"好感度は変わらなかった：現在好感度{fp}")
            else:
                print("好感度MAXです")
            you_died()

    else:
        print("満腹です")

# 成長処理
def grow():
    global fp
    global hp
    global stage

    time.sleep(10)
    print('青年期に入りました')
    stage = "青年期"
    if fp < 30:
        hp -= 30
        if hp < 0:
            hp = 0
            print(f"好感度が足りない!体力が30下がった!:現在の体力{hp}")
        else:
            print(f"好感度が足りない!体力が30下がった!:現在の体力{hp}")
        
    time.sleep(10)
    print('高年期に入りました')
    stage = "高齢期"
    if fp < 60:
        hp -= 30
        if hp < 0:
            hp = 0
            print(f"好感度が足りない!体力が30下がった!:現在の体力{hp}")
        else:
            print(f"好感度が足りない!体力が30下がった!:現在の体力{hp}")

# 死亡処理
def you_died():
    global hp
    global stage
    global fp
    global t1_alive

    if hp < 0 and stage == "若年期":
        if fp <= 30:
            print("僕なんかいなければ良かったんだ！！")
        elif fp <= 60:
            print("もっと愛して欲しかった...")
        elif fp > 60:
            print("ありがとう...短い間だったけど楽しかった！")
        
        # t1 スレッドを停止
        t1_alive = False

    if hp < 0 and stage == "青年期":
        if fp <= 30:
            print("青年期恨み言ー好感度30以下")
        elif fp <= 60:
            print("青年期恨み言ー好感度60以下")
        elif fp > 60:
            print("青年期恨み言ー好感度60以上")

        # t1 スレッドを停止
        t1_alive = False

    if hp < 0 and stage == "高齢期":
        print("ありがとう..わしはお主と出会えてよかった...")
        
        # t1 スレッドを停止
        t1_alive = False

def button_click3():
    # スレッドを作る
    thread1 = threading.Thread(target=danger)

    # スレッドの処理を開始
    thread1.start()

def main():
    t1 = threading.Thread(target=grow, daemon=True)
    t1.start()

    while True:
        if not t1_alive:
            break
        time.sleep(1)

    root = tkinter.Tk()
    button3 = tkinter.Button(root, text="danger", command=button_click3)
    button3.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
