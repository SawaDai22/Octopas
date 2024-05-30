import threading
import time
import tkinter
import random
from datetime import datetime
import requests

#初期体力上限
hpMax = 70

#体力
hp = hpMax

#好感度
fp = 0

#なでれる回数
pp = 10

#つつくのあたり回数
hit = 0

#つつける回数
entire = 10

#成長度
def grow():
    print(" スレッド:", threading.currentThread().getName())
    global fp
    global hp
    time.sleep(10)
    print('青年期に入りました')
    if fp < 30:
        hp -= 30
        if hp < 0:
            hp = 0
            print(f"好感度が足りない!体力が30下がった!:現在の体力{hp}")
        else:
            print(f"好感度が足りない!体力が30下がった!:現在の体力{hp}")
        
    time.sleep(10)
    print('高年期に入りました')
    if fp < 60:
        hp -= 30
        if hp < 0:
            hp = 0
            print(f"好感度が足りない!体力が30下がった!:現在の体力{hp}")
        else:
            print(f"好感度が足りない!体力が30下がった!:現在の体力{hp}")
    


#体力パック
def strength():
    global hp
    global fp
    if hp < hpMax:
        f=random.randint(0, 100)

        if f<30:
            hp += 6
            if hp > hpMax:
                hp = hpMax
                print(f"野菜を上げました：現在体力{hp}")
            else:
                print(f"野菜を上げました：現在体力{hp}")
            
            if fp < 100:
                fp += 1
                print(f"好感度が1上がった：現在好感度{fp}")
            else:
                print("好感度MAXです")
        elif f>=30 and f<50:
            hp += 8

            if hp > hpMax:
                hp = hpMax
                print(f"魚を上げました：現在体力{hp}")
            else:
                print(f"魚を上げました：現在体力{hp}")

            if fp < 100:
                fp += 2
                print(f"好感度が2上がった：現在好感度{fp}")
            else:
                print("好感度MAXです")
           
        elif f>=50:
            hp += 10
            if hp > hpMax:
                hp = hpMax
                print(f"肉を上げました：現在体力{hp}")
            else:
                print(f"肉を上げました：現在体力{hp}")

            if fp < 100:
                fp += 3
                print(f"好感度が3上がった：現在好感度{fp}")
            else:
                print("好感度MAXです")
       
    else:
        print("満腹です")

#好感度パック
def Favorability():
    global hp
    global fp
    if hp < hpMax:
        f=random.randint(0, 100)

        if f<30:
            hp += 3
            if hp > hpMax:
                hp = 100
                print(f"ドーナツを上げました：現在体力{hp}")
            else:
                print(f"ドーナツを上げました：現在体力{hp}")

            if fp < 100:
                fp += 8
                print(f"好感度が1上がった：現在好感度{fp}")
            else:
                print("好感度MAXです")

        elif f>=30 and f<50:
            hp += 2
            if hp > hpMax:
                hp = hpMax
                print(f"アイスクリームを上げました：現在体力{hp}")
            else:
                print(f"アイスクリームを上げました：現在体力{hp}")
            if fp < 100:
                fp += 6
                print(f"好感度が2上がった：現在好感度{fp}")
            else:
                print("好感度MAXです")
           
        elif f>=50:
            hp += 1
            if hp > hpMax:
                hp = hpMax
                print(f"チョコを上げました：現在体力{hp}")
            else:
                print(f"チョコを上げました：現在体力{hp}")
            if fp < 100:
                fp += 4
                print(f"好感度が3上がった：現在好感度{fp}")
            else:
                print("好感度MAXです")
       
    else:
        print("満腹です")

#諸刃の剣パック    
def danger():
    global hp
    global fp
    if hp < hpMax:
        f=random.randint(0, 100)

        if f<20:
            hp -= 10
            print(f"プラスチックを上げました：現在体力{hp}")
            fp -= 10
            if fp < 0:
                fp = 0
                print(f"好感度が10下がった：現在好感度{fp}")
            else:
                print(f"好感度が10下がった：現在好感度{fp}")

           
        elif f>=20 and f<40:
            hp -= 99999
            print(f"デスソースを上げました：現在体力{hp}")
            if fp < 100:
                print(f"好感度は変わらなかった：現在好感度{fp}")
            else:
                print("好感度MAXです")
           
        elif f>=40 and f<80:
            hp += 30
            if hp > hpMax:
                hp = hpMax
                print(f"ヨコエビを上げました：現在体力{hp}")
            else:
                print(f"ヨコエビを上げました：現在体力{hp}")
            if fp < 100:
                fp += 60
                print(f"好感度が60上がった：現在好感度{fp}")
            else:
                print("好感度MAXです")
        
        elif f>=80:
            hp += 60
            if hp > hpMax:
                hp = hpMax
                print(f"オキアミを上げました：現在体力{hp}")
            else:
                print(f"オキアミを上げました：現在体力{hp}")
            if fp < 100:
                fp += 30
                print(f"好感度が30上がった：現在好感度{fp}")
            else:
                print("好感度MAXです")

       
    else:
        print("満腹です")

#なでる機能
def pet():
    global fp
    global pp
    if pp > 0:
        if fp < 100:
            fp += 1
            pp -= 1
            print(f"フラップをなでた：残りなでられる回数{pp}")
            print(f"好感度が1上がった：現在好感度{fp}")
        else:
            print(f"フラップをなでた：残りなでられる回数{pp}")
            print("好感度MAXです")
    else:
        print("なでられません")

#つつく
def peck():
    global fp
    global hit
    global entire
    list = [0, 1]
    if hit == 0:
        f=random.randint(5, 9)
        hit = f
    
    if entire == 0:
        print("もうつつけません")
    else:
        probability = hit/entire
        weights = [1-probability,probability]
        result = random.choices(list, weights)
    
        extracted_result = result[0]
        if hit == 0:
            if fp == 0:
                print(f"{hit},{entire}")
                print("[0]")
                print(f"フラップは嫌がった,好感度は下がらなかった：現在の好感度{fp}")
                entire -= 1

            else:
                fp -= 7
                print(f"{hit},{entire}")
                print("[0]")
                if fp <0:
                    fp = 0
                    print(f"フラップは嫌がった,好感度7下がった：現在の好感度{fp}")
                else:
                    print(f"フラップは嫌がった,好感度7下がった：現在の好感度{fp}")
                entire -= 1
        elif hit-entire>0:
            if fp == 100:
                print(f"{hit},{entire}")
                print("[1]")
                print(f"フラップはよろこんだ,好感度は最大だ：現在の好感度{fp}")
                hit -= 1
                entire -= 1
            else:
                fp += 5
                print(f"{hit},{entire}")
                print("[1]")
                print(f"フラップはよろこんだ,好感度5上がった：現在の好感度{fp}")
                hit -= 1
                entire -= 1
        elif extracted_result == 1:
            if fp == 100:
                print(f"{hit},{entire}")
                print("[1]")
                print(f"フラップはよろこんだ,好感度は最大だ：現在の好感度{fp}")
                hit -= 1
                entire -= 1
            else:
                fp += 5
                print(f"{hit},{entire}")
                print(result)
                print(f"フラップはよろこんだ,好感度5上がった：現在の好感度{fp}")
                hit -= 1
                entire -= 1
            
        else : 
            if fp == 0:
                print(f"{hit},{entire}")
                print(result)
                print(f"フラップは嫌がった,好感度は下がらなかった：現在の好感度{fp}")
                entire -= 1
            else:
                fp -= 7
                print(f"{hit},{entire}")
                print(result)
                if fp <0:
                    fp = 0
                    print(f"フラップは嫌がった,好感度7下がった：現在の好感度{fp}")
                else:
                    print(f"フラップは嫌がった,好感度7下がった：現在の好感度{fp}")
#引っ張る
def pull():
    global fp
    list = [0,1]
    weights = [0.5,0.5]
    result = random.choices(list, weights)
    extracted_result = result[0]
    if extracted_result == 0:
        fp -= 7
        if fp < 0:
            fp = 0
            print(f"フラップは嫌がった,好感度7下がった：現在の好感度{fp}")
        else:
            print(f"フラップは嫌がった,好感度7下がった：現在の好感度{fp}")
    else:
        fp += 3
        if fp > 100:
            fp = 100
            print(f"フラップはまんざらでもない顔をした,好感度3上がった：現在の好感度{fp}")
        else:
            print(f"フラップはまんざらでもない顔をした,好感度3上がった：現在の好感度{fp}")


    


def get_weather(area_code):

  api_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"

# URLからデータを取得
  weather_data = requests.get(api_url).json()

# エリア名と予報データを取得
  area_name = weather_data[0]["timeSeries"][0]["areas"][0]["area"]["name"]
  timeSeries = weather_data[0]["timeSeries"][0]["timeDefines"]
  weather_series = weather_data[0]["timeSeries"][0]["areas"][0]["weathers"]

  weathers = ""

# 今日の日付を取得
  today = datetime.today().date()

# 出力内容の調整
  for time, weather in zip(timeSeries, weather_series):
     date = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S%z").date()
     if date == today:
        weathers = f"{date}{area_name}の天気は{weather}だよ"
        break  # 最初の一致でループを終了
    

# 区切り線とともに出力
  print("----------------------------------------------------------------------------------")
  print(weathers)
  print("----------------------------------------------------------------------------------")
       

    

   


def button_click1():
     # スレッドを作る
    thread1 = threading.Thread(target=strength)

    # スレッドの処理を開始
    thread1.start()

def button_click2():
     # スレッドを作る
    thread1 = threading.Thread(target=Favorability)

    # スレッドの処理を開始
    thread1.start()

def button_click3():
     # スレッドを作る
    thread1 = threading.Thread(target=danger)

    # スレッドの処理を開始
    thread1.start()

def button_click4():
     # スレッドを作る
    thread1 = threading.Thread(target=pet)

    # スレッドの処理を開始
    thread1.start()

def button_click5():
     # スレッドを作る
    thread1 = threading.Thread(target=peck)

    # スレッドの処理を開始
    thread1.start()

def button_click6():
     # スレッドを作る
    thread1 = threading.Thread(target=get_weather(130000))

    # スレッドの処理を開始
    thread1.start()

def button_click7():
     # スレッドを作る
    thread1 = threading.Thread(target=pull)

    # スレッドの処理を開始
    thread1.start()



# メイン
if __name__ == "__main__":
    print("スレッド:", threading.currentThread().getName())

    root = tkinter.Tk()
    button1 = tkinter.Button(root, text="体力パック", command=button_click1)
    button1.pack()
    button2 = tkinter.Button(root, text="好感度パック", command=button_click2)
    button2.pack()
    button3 = tkinter.Button(root, text="諸刃の剣パック", command=button_click3)
    button3.pack()
    button4 = tkinter.Button(root, text="なでる", command=button_click4)
    button4.pack()
    button5 = tkinter.Button(root, text="つつく", command=button_click5)
    button5.pack()
    button6 = tkinter.Button(root, text="天気予報", command=button_click6)
    button6.pack()
    button6 = tkinter.Button(root, text="引っ張る", command=button_click7)
    button6.pack()

    threadGrow = threading.Thread(target=grow)
    threadGrow.start()
    root.mainloop()


    

