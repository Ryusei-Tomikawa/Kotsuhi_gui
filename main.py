
import os
import csv
import sys
import gui
import datetime
import jpholiday

# py -m  pip install jpholiday

# 土日や祝日, 年休一斉取得日を判定する
def judge_holiday(dt_, judge_days_, yaskawa_holiday):

    date_list = []

    for i in range(dt_ + 1):
        # 土日の有無を場合
        if judge_days_.weekday() == 5 or judge_days_.weekday() == 6:
            print('この日は土曜 or 日曜日:=', judge_days_.day)
            h_d = True
        else:
            print('この日は土曜 or 日曜日ではない:=', judge_days_.day)
            h_d = False

        # 祝日の有無を判定
        res_holiday = jpholiday.is_holiday(datetime.date(judge_days_.year, judge_days_.month, judge_days_.day))
        if res_holiday == True:
            print('この日は祝日:=', judge_days_.day)
        elif res_holiday == False and h_d == False:
            print('この日は祝日ではない:=', judge_days_.day)

        # 年休一斉取得日の有無を判定
        for k in range(len(yaskawa_holiday)):
            y_dstr = str(yaskawa_holiday[k])
            yaskawa_days_ = datetime.date(int(y_dstr[0:4]), int(y_dstr[5:7]), int(y_dstr[8:10]))

            if h_d == False and res_holiday == False and (judge_days_.year == yaskawa_days_.year and judge_days_.month == yaskawa_days_.month and judge_days_.day == yaskawa_days_.day):
                print('この日は年休:=', yaskawa_days_)
                break
            elif h_d == False and res_holiday == False and k == (len(yaskawa_holiday) - 1):
                if ((judge_days_.month == yaskawa_days_.month and judge_days_.day != yaskawa_days_.day) or(judge_days_.month != yaskawa_days_.month and judge_days_.day == yaskawa_days_.day)) or (judge_days_.month != yaskawa_days_.month and judge_days_.day != yaskawa_days_.day):
                    print('この日は年休ではない:=', judge_days_)
                    j_dstr = str(judge_days_)
                    judge_datestr = j_dstr[0:4] + j_dstr[5:7] + j_dstr[8:10]
                    date_list.append(judge_datestr)
                else:
                    print('if文の条件以外が発生したから要修正')
            else:
                print('年休一斉取得日を判定中')

        judge_days_ = judge_days_ + datetime.timedelta(days=1)

    return date_list

# メイン関数
if __name__ == "__main__":
    # GUI作成
    gui.create_gui()

    f_y = f_m = f_d = t_y = t_m = t_d =  ''
    isKarihozon = 0

    f_y, f_m, f_d, t_y, t_m, t_d, isKarihozon = gui.get_ymd()

    print('from_year:=', f_y)
    print('from_month:=', f_m)
    print('from_day:=', f_d)
    print('to_year:=', t_y)
    print('to_month:=', t_m)
    print('to_day:=', t_d)
    print('isKarihozon:=', isKarihozon)

    # 土日祝日を探す為の変数
    from_days = datetime.datetime(f_y, f_m, f_d)
    to_days = datetime.datetime(t_y, t_m, t_d)
    dt = abs(from_days - to_days)

    judge_days = from_days

    # ファイルを読み込み、年休一斉取得日を取得
    # 絶対パスを取得
    abs_path = os.getcwd()
    with open(abs_path + '/holiday.txt') as f:
        y_holidays = f.readlines()
        y_holidays = [ii.replace('\n','') for ii in y_holidays]

    date_ = []
    # 入力した日付を土日、祝日、年休一斉取得日を除く
    date_ = judge_holiday(dt.days, judge_days, y_holidays)
    print('date:=', date_)
