import gui

# メイン関数
if __name__ == "__main__":
    gui.create_gui()

    f_y = 0
    f_m = 0
    f_d = 0
    t_y = 0
    t_m = 0
    t_d = 0
    isKarihozon = 0

    f_y, f_m, f_d, t_y, t_m, t_d, isKarihozon = gui.get_ymd()

    print('from_year:=', f_y)
    print('from_month:=', f_m)
    print('from_day:=', f_d)
    print('to_year:=', t_y)
    print('to_month:=', t_m)
    print('to_day:=', t_d)
    print('isKarihozon:=', isKarihozon)