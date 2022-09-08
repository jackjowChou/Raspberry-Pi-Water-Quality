# 測試 抽水機 功能
# 本程式執行後如果馬達有 轉大約兩秒後停止 代表程式、接線及馬達都完成了

import Rpi.GPIO as GPIO
import time
GPIO.cleanup()
PUMP_PIN = 38
GPIO.setmode( GPIO.BOARD ) # 使用的腳位號碼是 板子上的編號 不是 GPIO 的序號
GPIO.setup( PUMP_PIN, PGIO.OUT ) # 將 腳位 38 (GPIO編號是20) 設定為輸出腳位
GPIO.output( PUMP_PIN, GPIO.LOW ) # 設定 腳位輸出低電壓，如果腳位接的是 低電壓開通的繼電器 那抽水馬達會啟動，反之，使用高電壓開通的繼電器，那抽水馬達會停止
time.sleep( 2 ) # 這樣的狀態要執行多久才會執行 下一行指令

GPIO.output( PUMP_PIN, GPIO.HIGH )
time.sleep( 2 )

GPIO.cleanup()
