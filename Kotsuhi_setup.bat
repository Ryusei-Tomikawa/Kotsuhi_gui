@echo off
setlocal EnableDelayedExpansion

rem 交通費自動化申請セットアップの.bat

echo +-------------------------------------------------------+
echo;
echo 交通費自動化申請セットアップを開始します。
echo;
echo +-------------------------------------------------------+

:setup_loop

echo pythonのインストールを開始します。よろしいですか？（y/n）
echo ※すでにインストール済の場合は、"h"を入力してください。

set start=
set /p start= 

if %start% == y (
  rem echo %start%
  echo;
  echo pythonのインストールを開始します。
  echo; 
  call python-3.10.6-amd64

) else if %start% == n (
  echo;
  echo 交通費自動化申請セットアップを中止します。
  pause
  exit

) else if %start% == h (
  echo;
  echo インストール済なのでスキップします。
  echo;

) else (
  echo y or n or hを入力してください。
  goto setup_loop
) 

rem 現在接続しているWi-Fiの情報をテキストファイルに書き込む
type nul > wifi.txt
netsh wlan show interface >> wifi.txt

set count=0
for /f "skip=8 delims=" %%i in (wifi.txt) do (
    set ssid=%%i
    set /a count+=1
)&if !count!==1 goto :wf
:wf

set current_SSID=%ssid:~29%

timeout 2 /nobreak >nul

if %current_SSID% == Yaskawa_Wlan (
  echo;
  echo Yaskawa_Wlanに接続しているため、別のWi-Fi（寮やテザリングなど）に接続してください。
  echo ※Yaskawa_WlanやYaskawa_Mobileに接続している場合、次のステップで失敗します。
　echo; 
  pause
  exit
) else (
  echo;
  echo 現在 %current_SSID% に接続しています。
  rem 必要なライブラリ
  echo 交通費自動化申請に必要なライブラリをインストールします。
  timeout 2 /nobreak >nul
  py -m pip install pyautogui pywin32 Pillow opencv-python psutil jpholiday
  echo; 
  py -m pip list
  echo;
) 

echo +-------------------------------------------------------------------------+
echo;
echo 以下のライブラリがインストールされたか確認してください。
echo pyautogui pywin32 Pillow opencv-python psutil jpholiday
echo;
echo 無事インストールされていた場合、交通費自動化申請セットアップは終了です。
echo お疲れ様でした。
echo ※もし上手くいかなかった場合冨川まで
echo;
echo +------------------------------------------------------------------------+

pause
exit