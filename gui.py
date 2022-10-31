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
    
    title_label = ttk.Label(text=txt, justify="center", font=(f, f_num, "bold"))
    #左上が(0,0)
    title_label.place(x=x_, y=y_)

def karihozon_check():

    # check_click関数用のグローバル
    global yes_karihozon
    global no_karihozon

    yes_karihozon = BooleanVar(value = False)
    chk_yes_karihozon = ttk.Checkbutton(variable=yes_karihozon, text='仮保存する', command=lambda:check_click(yes_karihozon.get(), '仮保存する')) 
    chk_yes_karihozon.place(x=70, y=285)

    no_karihozon = BooleanVar(value = False)
    chk_no_karihozon = ttk.Checkbutton(variable=no_karihozon, text='仮保存しない', command=lambda:check_click(no_karihozon.get(), '仮保存しない')) 
    chk_no_karihozon.place(x=70, y=330)

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
    # to_monthの条件に関しては10月の時、１１月の申請できるようにするために+1している
    if date_now.month < from_month or date_now.month + 1 < to_month:
        error('その月はまだ入力できません')
        count -= 1
    elif (date_now.month == from_month or date_now.month == to_month) and (date_now.day < from_day or date_now.day < to_day):
        error('その日はまだ入力できません')
        count -= 1

    
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
        elif chk_txt == '仮保存する' and chk_state == False:
            # 仮保存するをFalse →仮保存しないを選択
            no_karihozon.set(True)
            isKarihozon_ = 0
        elif chk_txt == '仮保存しない' and chk_state == False:
            # 仮保存しないをFalse →仮保存するを選択
            yes_karihozon.set(True)
            isKarihozon_ = 1
        else:
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

        elif message == "GUIウィンドウを閉じてもよろしいですか？":
            close_res = messagebox.askyesno("最終確認", message)
            if close_res == True:
                sys.exit()
            else:
                messagebox.showinfo('再確認', '元の画面に戻ります')

def push_button(txt_, text_, width_, x_, y_):

    button = ttk.Button(text=txt_, width=width_, command=lambda:message_show(text_))
    button.place(x=x_, y=y_)

def window_delete():
    end_res = messagebox.askyesno("GUI終了", "GUIウィンドウを閉じてもよろしいですか？")
    if end_res == True:
        sys.exit()
    else:
        messagebox.showinfo('再確認', '元の画面に戻ります')

# GUI作成する関数
def create_gui():

    global root 

    #メインウィンドウ立ち上げ
    root = Tk()
    root.title('Tomikawa Create GUI')
    root.geometry('500x400')

    # ウィジェットの作成 padding=フレームの内側とWidgetとの間に空の領域を作成する
    frame = ttk.Frame(root, padding=10)
    frame.pack()

    # 現在日時取得
    date_now = datetime.datetime.now()
    today = datetime.datetime.today()

    if today.weekday() == 0:
        day_txt = '月'
    elif today.weekday() == 1:
        day_txt = '火'
    elif today.weekday() == 2:
        day_txt = '水'
    elif today.weekday() == 3:
        day_txt = '木'
    elif today.weekday() == 4:
        day_txt = '金'
    elif today.weekday() == 5:
        day_txt = '土'
    elif today.weekday() == 6:
        day_txt = '日'

    # タイトル
    write_label('安川電機  交通費申請自動化GUI', "MSゴシック", "20", 40, 55)
    #作成者
    write_label('作成者: 冨川 竜誠', "Times", "10", 370, 100)
    # 今日の日付
    write_label('今日の日付は', "MSゴシック", "12", 80, 130)
    write_label(str(date_now.year) + '年', "MSゴシック", "12", 190, 130)
    write_label(str(date_now.month) + '月', "MSゴシック", "12", 245, 130)
    write_label(str(date_now.day) + '日', "MSゴシック", "12", 285, 130)
    write_label(day_txt  + '曜日です', "MSゴシック", "12", 325, 130)

    #申請する日付
    write_label('申請する日付:', "Times", "12", 35, 180)

    # 安川画像表示
    yaskawa = tk.PhotoImage(file='yaskawa.png')
    canvas = tk.Canvas(bg="black", width=190, height=37)
    canvas.place(x=155, y=5)
    canvas.create_image(0, 0, image=yaskawa, anchor=tk.NW)

    #####################################　　日付処理　　　#########################################

    global count
    count = 0

    # 現在の年数から5年前まで
    year = []
    for i in range(6):
        year.append((date_now.year - 5) + i)
    # 年数入力 ～から
    entry('from_year', year, 4, 155, 180)
    # ～まで
    entry('to_year', year, 4, 155, 230)
    # 年ラベル ～から
    write_label('年', "Times", "12", 210, 180)
    # ～まで
    write_label('年', "Times", "12", 210, 230)

    # 1～12月
    month = []
    for i in range(12):
        month.append(i+1)
    # 月入力 ～から
    entry('from_month', month, 4, 235, 180)
    # ～まで
    entry('to_month', month, 4, 235, 230)
    # 月ラベル  ～から
    write_label('月', "Times", "12", 285, 180)
    # ～まで
    write_label('月', "Times", "12", 285, 230)

    # 1～31日
    day = []
    for i in range(31):
        day.append(i+1)
    # 日入力 ～から
    entry('from_day', day, 4, 310, 180)
    # ～まで
    entry('to_day', day, 4, 310, 230)
    # 日ラベル ～から
    write_label('日  から', "Times", "12", 360, 180)
    # ～まで
    write_label('日  まで', "Times", "12", 360, 230)

    ###########################################   仮保存する or しない  ###########################################

    # 仮保存チェックボタン押したときの処理（片方しか押せない）
    karihozon_check()

    ###########################################       ボタン処理        ############################################

    # 開始ボタン
    push_button("開始", "交通費自動化申請を開始しますか?", 20, 300, 280)
    #ウィンドウ閉じるボタン
    push_button("終了", "GUIウィンドウを閉じてもよろしいですか？", 20, 300, 330)

    # ✕ボタンを押すとウィンドウが閉じる
    root.protocol("WM_DELETE_WINDOW", window_delete)

    # ウィンドウの表示するための無限ループ
    root.mainloop()

