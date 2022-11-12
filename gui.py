import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# グローバルだらけできしょコード
# 日付と仮保存変数の初期化
from_year = from_month = from_day = to_year = to_month = to_day = isKarihozon_ = 0
auto_start_ = False

def judge_ymd(from_year_, from_month_, from_day_, to_year_, to_month_, to_day_):

    judge_ = False
    
    # 空かどうかのチェック
    judge_list_ = [from_year_, from_month_, from_day_, to_year_, to_month_, to_day_]
    for i in range(len(judge_list_)):
        if judge_list_[i] == '':
            error('日付が未入力です')
            return judge_

    if int(from_year_) - int(to_year_) > 0 or int(from_year_) - int(to_year_) < 0 :
        error('その年はまだ入力できません')
    elif int(from_month_) - int(to_month_) > 0:
        error('その月はまだ入力できません')
    elif int(from_month) < int(to_month) and int(from_day_) - int(to_day_) > 0:
        error('その日にちはまだ入力できません')
    else:
        judge_ = True

    return judge_

def set_ymd():
    
    ok_ = False
    f_y = f_m = f_d = t_y = t_m = t_d =  0
    global from_year_combobox
    global from_month_combobox
    global from_day_combobox
    global to_year_combobox
    global to_month_combobox
    global to_day_combobox

    f_y = from_year_combobox.get()
    f_m = from_month_combobox.get()
    f_d = from_day_combobox.get()
    t_y = to_year_combobox.get()
    t_m = to_month_combobox.get()
    t_d = to_day_combobox.get()

    ok_ = judge_ymd(f_y, f_m, f_d, t_y, t_m, t_d)

    if ok_ == True:
        global from_year
        global from_month
        global from_day
        global to_year
        global to_month
        global to_day

        from_year, from_month, from_day = int(f_y), int(f_m), int(f_d)
        to_year, to_month, to_day = int(t_y), int(t_m), int(t_d)

    return ok_
    
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
    chk_yes_karihozon.place(x=70, y=245)

    no_karihozon = BooleanVar(value = True)
    chk_no_karihozon = ttk.Checkbutton(variable=no_karihozon, text='仮保存しない', command=lambda:check_click(no_karihozon.get(), '仮保存しない')) 
    chk_no_karihozon.place(x=70, y=280)

def error(message):
        messagebox.showerror('Error message', message)

# 日付入力する関数
def input_date(txt_, list_, width_, x_, y_, init_day):

    global from_year_combobox
    global from_month_combobox
    global from_day_combobox
    global to_year_combobox
    global to_month_combobox
    global to_day_combobox

    if txt_ == 'from_year':
        from_year_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values = list_)
        from_year_combobox.place(x=x_, y=y_)
        from_year_combobox.set(str(init_day))

    elif txt_ == 'to_year':
        to_year_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values = list_)
        to_year_combobox.place(x=x_, y=y_)
        to_year_combobox.set(str(init_day))

    elif txt_ == 'from_month':
        from_month_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values=list_)
        from_month_combobox.place(x=x_, y=y_)
        from_month_combobox.set(str(init_day))

    elif txt_ == 'to_month':
        to_month_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values = list_)
        to_month_combobox.place(x=x_, y=y_)
        to_month_combobox.set(str(init_day))

    elif txt_ == 'from_day':
        from_day_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values = list_)
        from_day_combobox.place(x=x_, y=y_)
        from_day_combobox.set(str(init_day))

    elif txt_ == 'to_day':
        to_day_combobox = ttk.Combobox(width= width_, height = len(list_), justify="center", values = list_)
        to_day_combobox.place(x=x_, y=y_)
        to_day_combobox.set(str(init_day))
        
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
        global auto_start_

        ok = False

        # 自動化するかどうかの最終確認
        if message == "交通費自動化申請を開始しますか?":
             auto_res = messagebox.askyesno("最終確認", message)
             if auto_res == True:
                auto_start_ = True
                ok = set_ymd()
                if ok == True:
                    root.destroy()

        elif message == "GUIウィンドウを閉じてもよろしいですか？":
            close_res = messagebox.askyesno("最終確認", message)
            if close_res == True:
                auto_start_ = False
                # mainloopを抜ける処理
                root.destroy()
                
        elif message == '交通費申請を開始します.マウスやキーボードは触れないでください.':
            messagebox.showwarning('注意', message)
        
        elif message == '交通費自動化申請を終了しました。'
            messagebox.showinfo('終了通知', message)
           
def push_button(txt_, width_, x_, y_):

    button = ttk.Button(text=txt_, width=width_)
    button.bind('<Return>', lambda event:message_show(txt_))
    button.bind('<Button-1>', lambda event:message_show(txt_))
    button.place(x=x_, y=y_)
    
# GUI作成する関数
def create_gui():

    global root 

    #メインウィンドウ立ち上げ
    root = Tk()
    root.title('YFTS22 交通費申請自動化GUI')
    root.geometry('490x370')
    root.geometry('+425+0')
    root.resizable(width=False, height=False)

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

    # 安川画像表示
    path=__file__
    name = path.rstrip('auto_gui.py')+'yaskawa.png'
    yaskawa = tk.PhotoImage(file=name)
    canvas = tk.Canvas(bg="black", width=190, height=37)
    canvas.place(x=155, y=5)
    canvas.create_image(0, 0, image=yaskawa, anchor=tk.NW)
    
    # タイトル
    write_label('YFTS22 交通費申請自動化GUI', "MSゴシック", "20", 40, 50)
    #作成者
    write_label('作成者: 冨川 竜誠', "Times", "10", 365, 5)
    # 今日の日付
    write_label('今日の日付は', "MSゴシック", "12", 85, 105)
    write_label(str(date_now.year) + '年', "MSゴシック", "12", 195, 105)
    write_label(str(date_now.month) + '月', "MSゴシック", "12", 250, 105)
    write_label(str(date_now.day) + '日', "MSゴシック", "12", 290, 105)
    write_label(day_txt  + '曜日です', "MSゴシック", "12", 320, 105)

    # 申請する日付
    write_label('申請する日付:', "Times", "12", 35, 150)
    
    # ※記載
    write_label('※ウィンドウは動かさないことを推奨します。', "MSゴシック", "9", 120, 320)

    #####################################　　日付処理　　　#########################################


    monday = today - datetime.timedelta(days=today.weekday())
    friday = today + datetime.timedelta(days=4)

    # 現在の年数から5年後まで
    year = []
    for i in range(6):
        year.append((date_now.year - 5) + i)
    # 年数入力 ～から
    input_date('from_year', year, 4, 155, 150, int(monday.year))
    # ～まで
    input_date('to_year', year, 4, 155, 200, int(friday.year))
    # 年ラベル ～から
    write_label('年', "Times", "12", 210, 150)
    # ～まで
    write_label('年', "Times", "12", 210, 200)

    # 1～12月
    month = []
    for i in range(12):
        month.append(i+1)
    # 月入力 ～から
    input_date('from_month', month, 4, 235, 150, int(monday.month))
    # ～まで
    input_date('to_month', month, 4, 235, 200, int(friday.month))
    # 月ラベル  ～から
    write_label('月', "Times", "12", 285, 150)
    # ～まで
    write_label('月', "Times", "12", 285, 200)

    # 1～31日
    day = []
    for i in range(31):
        day.append(i+1)
    # 日入力 ～から
    input_date('from_day', day, 4, 310, 150, int(monday.day))
    # ～まで
    input_date('to_day', day, 4, 310, 200, int(friday.day))
    # 日ラベル ～から
    write_label('日  から', "Times", "12", 360, 150)
    # ～まで
    write_label('日  まで', "Times", "12", 360, 200)
    
    ###########################################   仮保存する or しない  ###########################################

    # 仮保存チェックボタン押したときの処理（片方しか押せない）
    karihozon_check()

    ###########################################       ボタン処理        ############################################

    # 開始ボタン
    push_button("開始", 20, 300, 245)
    #ウィンドウ閉じるボタン
    push_button("終了", 20, 300, 285)

    # ×ボタンでウィンドウ消す
    root.protocol("WM_DELETE_WINDOW", root.destroy())
    
    # ウィンドウの表示するための無限ループ
    root.mainloop()


