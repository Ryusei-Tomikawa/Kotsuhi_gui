import sys
import datetime
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# グローバルだらけできしょコード

def write_label(txt, f, f_num, x_, y_):
    
    title_label = ttk.Label(text=txt, font=(f, f_num, "bold"))
    #左上が(0,0)
    title_label.place(x=x_, y=y_)

def error(message):
        messagebox.showerror('エラーメッセージ', message)

def get_combobox(text_, num):

    
    # 現在日時取得
    date_now = datetime.datetime.now()

    # 毎回初期化は正直あれやけどまぁいいや
    from_year = 0
    to_year = 0
    from_month = 0
    to_month = 0
    from_day = 0
    # 特に意味はない
    to_day = date_now.day 

    if text_ == 'from_year':
        from_year = num
    elif text_ == 'to_year':
        to_year = num
    elif text_ == 'from_month':
        from_month = num
    elif text_ == 'to_month':
        to_month = num
    elif text_ == 'from_day':
        from_day = num
    elif text_ == 'to_day':
        to_day = num

    global count
    count += 1

    if date_now.year <  from_year or date_now.year < to_year:
        error('その年数はまだ入力できません')
    elif date_now.month < from_month or date_now.month < to_month:
        error('その月はまだ入力できません')
    
# 日付入力する関数　他になんかいい方法あるかな～
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
        
        global check_state1
        global check_state2

        global chk_state_
        chk_state_ = chk_state

        if chk_txt == '仮保存する' and chk_state == True:
            check_state2.set(False)

        elif  chk_txt == '仮保存しない' and chk_state == True:
            check_state1.set(False)

        else:
            check_state1.set(False)
            check_state2.set(False)

def message_show(message):
        
        global chk_state_
        global count

        day_ = False
        store_ = False

        # 日付に関するエラー処理 入力回数: 6回
        if count < 6:
            error('入力項目が足りません')
        elif count >= 6:
            day_ = True

        # 仮保存におけるエラー処理
        if chk_state_ == False:
            error('仮保存選択がされていません')
            store_ = False
        elif chk_state_ == True:
            store_ = True


        # 自動化するかどうかの最終確認
        if message == "交通費自動化申請を開始しますか" and day_ == True and store_ == True:
             auto_res = messagebox.askyesno("最終確認", message)
             if auto_res == True:
                print('ここで自動化プログラムを実行!')
             else:
                messagebox.showinfo('再確認', '元の画面に戻ります')

        elif message == "ウィンドウを閉じてもよろしいですか？":
            close_res = messagebox.askyesno("最終確認", message)
            if close_res == True:
                sys.exit()
            else:
                messagebox.showinfo('再確認', '元の画面に戻ります')

def push_button(txt_, text_, width_, x_, y_):

    button = ttk.Button(text=txt_, width=width_, command=lambda:message_show(text_))
    button.place(x=x_, y=y_)

# メイン関数の詳細
def main():

    #メインウィンドウ立ち上げ
    root = Tk()
    root.title('Tomikawa Create GUI')
    root.geometry('500x360')

    # フレームの作成 padding=フレームの内側とWidgetとの間に空の領域を作成する
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

    # 2030年まで
    year = []
    for i in range(9):
        year.append(2022 + i)
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

    # 他になんかいい書き方あるかなぁ

    global chk_state_
    global check_state1
    global check_state2

    chk_state_ = False

    check_state1 = BooleanVar(value = False)
    chk1 = ttk.Checkbutton(variable=check_state1, text='仮保存する', command=lambda:check_click(check_state1.get(), '仮保存する')) 
    chk1.place(x=70, y=235)

    check_state2 = BooleanVar(value = False)
    chk2 = ttk.Checkbutton(variable=check_state2, text='仮保存しない', command=lambda:check_click(check_state2.get(), '仮保存しない')) 
    chk2.place(x=70, y=280)

    ###########################################       ボタン処理        ############################################

    # 開始ボタン
    push_button("開始", "交通費自動化申請を開始しますか", 20, 300, 230)
    #ウィンドウ閉じるボタン
    push_button("終了", "ウィンドウを閉じてもよろしいですか？", 20, 300, 280)

    # ウィンドウの表示するための無限ループ
    root.mainloop()

# メイン関数
if __name__ == "__main__":
    main()
