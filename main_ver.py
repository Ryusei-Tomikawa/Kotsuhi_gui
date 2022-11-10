
import os
import sys
import gui
import datetime
import jpholiday

# py -m  pip install jpholiday

# 土日や祝日, 年休一斉取得日を判定する
########  スマートver #######
def judge_holiday(judge_, yaskawa_holiday):

########  要求ver   #######
#def judge_holiday(judge_year, judge_month, judge_day, yaskawa_holiday):
####### 要求verはこれを入れること　スマートverはこれいらない #####
    #judge_ = datetime.datetime(judge_year, judge_month, judge_day)

    judge_holiday = False

    date_list = []

    # 土日の有無を場合
    if judge_.weekday() == 5 or judge_.weekday() == 6:
        print('この日は土曜 or 日曜日:=', judge_.day)
        h_d = True
        judge_holiday = True

    else:
        print('この日は土曜 or 日曜日ではない:=', judge_.day)
        h_d = False
        judge_holiday = False

    # 祝日の有無を判定
    res_holiday = jpholiday.is_holiday(datetime.date(judge_.year, judge_.month, judge_.day))

    if res_holiday == True:
        print('この日は祝日:=', judge_.day)
        judge_holiday = True

    elif res_holiday == False and h_d == False:
        print('この日は祝日ではない:=', judge_.day)
        judge_holiday = False

    # 年休一斉取得日の有無を判定
    for k in range(len(yaskawa_holiday)):
        y_dstr = str(yaskawa_holiday[k])
        yaskawa_days_ = datetime.date(int(y_dstr[0:4]), int(y_dstr[5:7]), int(y_dstr[8:10]))

        if h_d == False and res_holiday == False and (judge_.year == yaskawa_days_.year and judge_.month == yaskawa_days_.month and judge_.day == yaskawa_days_.day):
            print('この日は年休:=', yaskawa_days_)
            judge_holiday = True
            break

        elif h_d == False and res_holiday == False and k == (len(yaskawa_holiday) - 1):
            if ((judge_.month == yaskawa_days_.month and judge_.day != yaskawa_days_.day) or(judge_.month != yaskawa_days_.month and judge_.day == yaskawa_days_.day)) or (judge_.month != yaskawa_days_.month and judge_.day != yaskawa_days_.day):
                print('この日は年休ではない:=', judge_)
                judge_holiday = False

            else:
                print('if文の条件以外が発生したから要修正')
        else:
            print('年休一斉取得日を判定中')

    return judge_holiday

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
    abs_path = os.getcwd()
    with open(abs_path + '/holiday.txt') as f:
        y_holidays = f.readlines()
        y_holidays = [ii.replace('\n','') for ii in y_holidays]

    # 土日、祝日、年休一斉取得日があるかどうかのフラグ(ある場合:True, ない場合:False)
    JD = False

    date = []
    # 入力した日付から土日、祝日、年休一斉取得日を除く
    for i in range(dt.days + 1):
        ########  スマートver ######
        JD = judge_holiday(judge_days, y_holidays)

        #######   要求ver #####
        #JD = judge_holiday(judge_days.year, judge_days.month, judge_days.day, y_holidays)
        if JD == True:
            print('この日は申請しません')
        else:
            print('この日は申請します')
            date.append(judge_days)
            #print('judge_days:=', judge_days)

        judge_days = judge_days + datetime.timedelta(days=1)