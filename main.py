import gui
import datetime
import jpholiday

# py -m  pip install jpholiday

# 土日や祝日を判定する
def judge_holiday(dt_, judge_days_):

    date = []

    for i in range(dt_):
        # 土日の有無を場合
        if judge_days_.weekday() == 5 or judge_days_.weekday() == 6:
            print('satur or sun days:=', judge_days_.day)
            h_d = True
        else:
            print('Not satur or sun days:=', judge_days_.day)
            h_d = False

        # 祝日の有無を判定
        res_holiday = jpholiday.is_holiday(datetime.date(judge_days_.year, judge_days_.month, judge_days_.day))
        if res_holiday == True:
            print('holiday:=', judge_days_.day)
        elif res_holiday == False and h_d == False:
            print('not holiday:=', judge_days_.day)
            date.append(judge_days_)

        judge_days_ = judge_days_ + datetime.timedelta(days=1)

    return date



# メイン関数
if __name__ == "__main__":
    # GUI作成
    gui.create_gui()

    f_y = f_m = f_d = t_y = t_m = t_d =  0
    isKarihozon = 2

    f_y, f_m, f_d, t_y, t_m, t_d, isKarihozon = gui.get_ymd()


    print('from_year:=', f_y)
    print('from_month:=', f_m)
    print('from_day:=', f_d)
    print('to_year:=', t_y)
    print('to_month:=', t_m)
    print('to_day:=', t_d)
    print('isKarihozon:=', isKarihozon)

    from_days = datetime.datetime(f_y, f_m, f_d)
    to_days = datetime.datetime(t_y, t_m, t_d)
    dt = abs(from_days - to_days)

    judge_days = from_days

    date_ = []

    # 入力した日付を土日、祝日を除く
    date_ = judge_holiday(dt.days, judge_days)

    if len(date_) > 5:
        print('申請できない')
    else:
        for i in range(len(date_)):
            d1 = datetime.date(date_[i].year, date_[i].month, date_[i].day)
            d1str = str(d1)
            date = d1str[0:4] + d1str[5:7] + d1str[8:10]
            print('date:=', date)