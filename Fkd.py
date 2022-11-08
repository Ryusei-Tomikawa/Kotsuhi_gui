from Sub import AutoImputKotsuhi_SubPro
import time
import datetime
import pyautogui
import traceback
import sys
import gui
import jpholiday

#11013AZLE0148546   666
#11013AZLE0148146   650

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

def main():
    
    print('\n\n')
    print(' ----FkdAutoKotsuhiYFTS.py version2.5----')
    print('                           released on 2022/10/07')
    print('\n\n')

    # 変数初期化
    f_y = f_m = f_d = t_y = t_m = t_d = isKarihozon = 0
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

    # 入力初日
    # d1 = datetime.date(YY,MM,DD)
    # d1str = str(d1)
    # date = d1str[0:4] + d1str[5:7] + d1str[8:10]
    
    from_days = datetime.datetime(f_y, f_m, f_d)
    to_days = datetime.datetime(t_y, t_m, t_d)
    dt = abs(from_days - to_days)
    
    judge_date_ = []
    judge_days = from_days
    # 入力した日付を土日、祝日を除く
    judge_date_ = judge_holiday(dt.days, judge_days)
    if len(judge_date_) > 5:
        gui.error('5日以上は申請できません。')
        sys.exit()
        
    elif len(judge_date_) <= 5 and auto_start == True:
        
        gui.message_show('交通費申請を開始します.マウスやキーボードは触れないでください.')
    
        # 自動化開始前のスリープ
        time.sleep(2.0)

        # 複写の伝票番号を読み込む
        AutoImputKotsuhi_SubPro.NoDenpyoCheck()

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

        #インプット
        # 入力初日 
        j_d = datetime.date(judge_date_[0].year, judge_date_[0].month, judge_date_[0].day)
        j_dstr = str(j_d)
        j_date = j_dstr[0:4] + j_dstr[5:7] + j_dstr[8:10]
        scl = AutoImputKotsuhi_SubPro.ImputDate(j_date, 300)
        
        for i in range(len(judge_date_)):
            d1 = datetime.date(judge_date_[i+1].year, judge_date_[i+1].month, judge_date_[i+1].day)
            d1str = str(d1)
            date = d1str[0:4] + d1str[5:7] + d1str[8:10]
            print('date:=', date)
            AutoImputKotsuhi_SubPro.clickTab(i+2)
            time.sleep(1.5)
            AutoImputKotsuhi_SubPro.ImputDate(date, scl)

        pyautogui.scroll(10000)
        time.sleep(0.5)
        if isKarihozon == 1:
            AutoImputKotsuhi_SubPro.click('Karihozon.png',0.95,0)

        # 終了処理
        gui.end()
        
    else:
        print('Input value error')


if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit()
        
        
# 入力初日以降
# for ii in range(dt.days):
#     d1 = d1 + datetime.timedelta(days=1)
#     d1str = str(d1)
#     date = d1str[0:4] + d1str[5:7] + d1str[8:10]
#     AutoImputKotsuhi_SubPro.clickTab(ii+2)
#     time.sleep(1.5)
#     AutoImputKotsuhi_SubPro.ImputDate(date,scl)