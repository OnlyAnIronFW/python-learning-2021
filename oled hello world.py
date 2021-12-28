# https://bxy.dfrobot.com.cn/mpy-display
from mpython import *

oled.DispChar('你好世界', 38, 0)         #先写入缓存区，在(38,0)处显示'你好世界'
oled.DispChar('hello,world', 32, 16)     #先写入缓存区，在(32,16)处显示'hello,world'
oled.DispChar('안녕하세요', 35, 32)         #先写入缓存区，在(35,32)处显示'안녕하세요'
oled.DispChar('こんにちは世界', 24, 48)  #先写入缓存区，在(24,48)处显示'こんにちは世界'
oled.show()                              #显示画面
