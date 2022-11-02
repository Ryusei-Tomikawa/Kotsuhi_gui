from Sub import AutoImputKotsuhi_SubPro
import time
import datetime
import pyautogui
import os
import pyperclip
import sys
import gui

#11013AZLE0148546   666
#11013AZLE0148146   650

print('\n\n')
print(' ----FkdAutoKotsuhiYFTS.py version2.5----')
print('                           released on 2022/10/07')
print('\n\n')

# 変数初期化
f_y = 0
f_m = 0
f_d = 0
t_y = 0
t_m = 0
t_d = 0
isKarihozon = 2
auto_start = False

# GUI起動
gui.create_gui()

# GUIで入力した日付, 仮保存有無を取得
f_y, f_m, f_d, t_y, t_m, t_d, isKarihozon, auto_start = gui.get_ymd()

print('from_year:=', f_y)
print('from_month:=', f_m)
print('from_day:=', f_d)
print('to_year:=', t_y)
print('to_month:=', t_m)
print('to_day:=', t_d)
print('isKarihozon:=', isKarihozon)
print('auto_start:=', auto_start)

YY = f_y
MM = f_m
DD = f_d

f_dt = datetime.datetime(year=f_y, month=f_m, day=f_d)
t_dt = datetime.datetime(year=t_y, month=t_m, day=t_d)
dt = abs(f_dt - t_dt)

# 自動化開始前のスリープ
time.sleep(2.0)

# 複写の伝票番号を読み込む
# dtの値によって伝票番号を分ける
# 2日だけ申請の場合：この伝票番号を複製、5日申請の場合、この伝票番号を複製→計5通り
AutoImputKotsuhi_SubPro.NoDenpyoCheck(dt.days)

if YY > 0 and MM > 0 and DD > 0 and (isKarihozon == 0 or isKarihozon == 1) and auto_start == True:
    AutoImputKotsuhi_SubPro.OpenBrowser('ie')
    AutoImputKotsuhi_SubPro.check('MainPage.png',0.5,20,0.8)
    AutoImputKotsuhi_SubPro.OpenNWFS()
    AutoImputKotsuhi_SubPro.WindowSetting()

    #Examを持ってくる
    ND1,ND2 = AutoImputKotsuhi_SubPro.LoadNoDenpyo()

    #新規起票起動
    AutoImputKotsuhi_SubPro.check('WfTop.png',0.5,10,0.8)
    AutoImputKotsuhi_SubPro.ShinkiKihyou()

    #初期入力
    AutoImputKotsuhi_SubPro.FirstImput()

    #複写検索
    AutoImputKotsuhi_SubPro.Fukusha(ND1,ND2)

    #日付の処理
    d1 = datetime.date(YY,MM,DD)
    d1str = str(d1)
    date = d1str[0:4] + d1str[5:7] + d1str[8:10]

    #インプット
    scl = AutoImputKotsuhi_SubPro.ImputDate(date,300)
    for ii in range(dt.days):
        d1 = d1 + datetime.timedelta(days=1)
        d1str = str(d1)
        date = d1str[0:4] + d1str[5:7] + d1str[8:10]
        AutoImputKotsuhi_SubPro.clickTab(ii+2)
        time.sleep(1.5)
        AutoImputKotsuhi_SubPro.ImputDate(date,scl)

    pyautogui.scroll(10000)
    time.sleep(0.5)
    if isKarihozon == 1:
        AutoImputKotsuhi_SubPro.click('Karihozon.png',0.95,0)

    # 終了処理
    gui.end()
    
else:
    print('Inpur value error')
    sys.exit()

sys.exit()