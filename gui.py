import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# グローバルだらけできしょコード

# 日付と仮保存変数の初期化
from_year = 0
to_year = 0
from_month = 0
to_month = 0
from_day = 0
to_day = 0
isKarihozon_ = 2

# main.pyで値を取得する用
def get_ymd():
    global from_year
    global from_month
    global from_day
    global to_year
    global to_month
    global to_day
    global isKarihozon_

    return from_year, from_month, from_day, to_year, to_month, to_day, isKarihozon_

def write_label(txt, f, f_num, x_, y_):
    
    title_label = ttk.Label(text=txt, font=(f, f_num, "bold"))
    #左上が(0,0)
    title_label.place(x=x_, y=y_)

def karihozon_check():

    # check_click関数用のグローバル
    global yes_karihozon
    global no_karihozon

    yes_karihozon = BooleanVar(value = False)
    chk_yes_karihozon = ttk.Checkbutton(variable=yes_karihozon, text='仮保存する', command=lambda:check_click(yes_karihozon.get(), '仮保存する')) 
    chk_yes_karihozon.place(x=70, y=235)

    no_karihozon = BooleanVar(value = False)
    chk_no_karihozon = ttk.Checkbutton(variable=no_karihozon, text='仮保存しない', command=lambda:check_click(no_karihozon.get(), '仮保存しない')) 
    chk_no_karihozon.place(x=70, y=280)

def error(message):
        messagebox.showerror('エラーメッセージ', message)

# 日付入力した際のCallback 
def get_combobox(text_, num):

    # 現在日時取得
    date_now = datetime.datetime.now()

    global from_year
    global from_month
    global from_day
    global to_year
    global to_month
    global to_day

    if text_ == 'from_year':
        from_year = num
        from_day = date_now.day
        to_day = date_now.day
    elif text_ == 'to_year':
        to_year = num
        from_day = date_now.day
        to_day = date_now.day
    elif text_ == 'from_month':
        from_month = num
        from_day = date_now.day
        to_day = date_now.day
    elif text_ == 'to_month':
        to_month = num
        from_day = date_now.day
        to_day = date_now.day
    elif text_ == 'from_day':
        from_day = num
    elif text_ == 'to_day':
        to_day = num

    global count
    count += 1

    #print('from_year:=', from_year)
    #print('from_month:=', from_month)
    #print('from_day:=', from_day)
    #print('to_year:=', to_year)
    #print('to_month:=', to_month)
    #print('to_day:=', to_day)


    # 年数がエラーかつ日付が正確に打てた場合→countが＋１にならないためバグ発生
    # ex. 2025(out) 10(ok) の場合、2025がoutだから10が性格でもcountが＋１にならない
    # ここのエラー処理は拘るべきだと思うけど。。。

    if date_now.year <  from_year or date_now.year < to_year:
        error('その年数はまだ入力できません')
        count -= 1
    elif date_now.month < from_month or date_now.month < to_month:
        error('その月はまだ入力できません')
        count -= 1
    elif (date_now.month == from_month or date_now.month == to_month) and (date_now.day < from_day or date_now.day < to_day):
        error('その日はまだ入力できません')

    
# 日付入力する関数
def entry(txt_, list_, width_, x_, y_):

    variable = IntVar()
    variable.set('')

    if txt_ == 'from_year':
        from_year_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values = list_, textvariable = variable)
        from_year_combobox.place(x=x_, y=y_)
        from_year_combobox.bind('<<ComboboxSelected>>', lambda e: get_combobox(txt_, variable.get()))
    elif txt_ == 'to_year':
        to_year_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values = list_, textvariable = variable)
        to_year_combobox.place(x=x_, y=y_)
        to_year_combobox.bind('<<ComboboxSelected>>', lambda e: get_combobox(txt_, variable.get()))
    elif txt_ == 'from_month':
        from_month_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values=list_, textvariable = variable)
        from_month_combobox.place(x=x_, y=y_)
        from_month_combobox.bind('<<ComboboxSelected>>', lambda e: get_combobox(txt_, variable.get()))
    elif txt_ == 'to_month':
        to_month_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values = list_, textvariable = variable)
        to_month_combobox.place(x=x_, y=y_)
        to_month_combobox.bind('<<ComboboxSelected>>', lambda e: get_combobox(txt_, variable.get()))
    elif txt_ == 'from_day':
        from_day_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values = list_, textvariable = variable)
        from_day_combobox.place(x=x_, y=y_)
        from_day_combobox.bind('<<ComboboxSelected>>', lambda e: get_combobox(txt_, variable.get()))
    elif txt_ == 'to_day':
        to_day_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values = list_, textvariable = variable)
        to_day_combobox.place(x=x_, y=y_)
        to_day_combobox.bind('<<ComboboxSelected>>', lambda e: get_combobox(txt_, variable.get()))


def check_click(chk_state, chk_txt):
        
        
        global yes_karihozon
        global no_karihozon


        # get_ymdk関数用のグルーバル変数
        global isKarihozon_

        if chk_txt == '仮保存する' and chk_state == True:
            # 仮保存しないをFalse →仮保存する選択
            no_karihozon.set(False)
            isKarihozon_ = 1

        elif  chk_txt == '仮保存しない' and chk_state == True:
            # 仮保存するをFalse →仮保存しない選択
            yes_karihozon.set(False)
            isKarihozon_ = 0

        else:
            # 両方をFalse
            yes_karihozon.set(False)
            no_karihozon.set(False)

def message_show(message):

        # destroy用
        global root

        # 日付エラー処理用
        global count
        # 仮保存エラー処理用
        global isKarihozon_

        day_ = False
        store_ = False

        # 日付に関するエラー処理 入力回数: 6回
        if count < 6:
            error('入力項目が足りません')
        elif count >= 6:
            day_ = True

        # 仮保存におけるエラー処理
        if isKarihozon_ == 2:
            error('仮保存選択がされていません')
            store_ = False
        elif isKarihozon_ == 0 or isKarihozon_ == 1:
            store_ = True

        # 自動化するかどうかの最終確認
        if message == "交通費自動化申請を開始しますか?" and day_ == True and store_ == True:
             auto_res = messagebox.askyesno("最終確認", message)
             if auto_res == True:
                # mainloopを抜ける処理
                root.destroy()
             else:
                messagebox.showinfo('再確認', '元の画面に戻ります')

        elif message == "ウィンドウを閉じてもよろしいですか？":
            close_res = messagebox.askyesno("最終確認", message)
            if close_res == True:
                # mainloopを抜ける処理
                root.destroy()
            else:
                messagebox.showinfo('再確認', '元の画面に戻ります')

def push_button(txt_, text_, width_, x_, y_):

    button = ttk.Button(text=txt_, width=width_, command=lambda:message_show(text_))
    button.place(x=x_, y=y_)

# GUI作成する関数
def create_gui():

    global root 

    #メインウィンドウ立ち上げ
    root = Tk()
    root.title('Tomikawa Create GUI')
    root.geometry('500x360')

    # ウィジェットの作成 padding=フレームの内側とWidgetとの間に空の領域を作成する
    frame = ttk.Frame(root, padding=10)
    frame.pack()

    # タイトル
    write_label('安川電機  交通費申請自動化GUI', "MSゴシック", "20", 40, 50)
    #作成者
    write_label('作成者: 冨川 竜誠', "Times", "10", 370, 95)
    #申請する日付
    write_label('申請する日付:', "Times", "12", 20, 130)

    # 安川画像表示
    yaskawa = tk.PhotoImage(file='yaskawa.png')
    canvas = tk.Canvas(bg="black", width=190, height=37)
    canvas.place(x=155, y=5)
    canvas.create_image(0, 0, image=yaskawa, anchor=tk.NW)

    #####################################　　日付処理　　　#########################################

    global count
    count = 0

    # 現在の年数から5年前まで
    # 現在日時取得
    date_now = datetime.datetime.now()

    year = []
    for i in range(6):
        year.append((date_now.year - 5) + i)
    # 年数入力 ～から
    entry('from_year', year, 4, 140, 130)
    # ～まで
    entry('to_year', year, 4, 140, 180)
    # 年ラベル ～から
    write_label('年', "Times", "12", 195, 130)
    # ～まで
    write_label('年', "Times", "12", 195, 180)

    # 1～12月
    month = []
    for i in range(12):
        month.append(i+1)
    # 月入力 ～から
    entry('from_month', month, 4, 220, 130)
    # ～まで
    entry('to_month', month, 4, 220, 180)
    # 月ラベル  ～から
    write_label('月', "Times", "12", 270, 130)
    # ～まで
    write_label('月', "Times", "12", 270, 180)

    # 1～31日
    day = []
    for i in range(31):
        day.append(i+1)
    # 日入力 ～から
    entry('from_day', day, 4, 295, 130)
    # ～まで
    entry('to_day', day, 4, 295, 180)
    # 日ラベル ～から
    write_label('日  から', "Times", "12", 345, 130)
    # ～まで
    write_label('日  まで', "Times", "12", 345, 180)

    ###########################################   仮保存する or しない  ###########################################

    # 仮保存チェックボタン押したときの処理（片方しか押せない）
    karihozon_check()

    ###########################################       ボタン処理        ############################################

    # 開始ボタン
    push_button("開始", "交通費自動化申請を開始しますか?", 20, 300, 230)
    #ウィンドウ閉じるボタン
    push_button("終了", "ウィンドウを閉じてもよろしいですか？", 20, 300, 280)

    # ウィンドウの表示するための無限ループ
    root.mainloop()

