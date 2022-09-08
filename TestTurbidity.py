# 水質檢測感應器 測試
import smbus
import time

address = 0x48
bus = smbus.SMBus( 1 )

while True:
  value = bus.read_byte( address )
  print( value )
  time.sleep( 1 )
