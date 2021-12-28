from mpython import *
import time
import music
import json

while True:
  msg=input()
  try:
    v = json.loads(msg)
    rgb_v = int(v["rgb"])
    buzz_v = int(v["buzz"])
    rgb[0]=(rgb_v, rgb_v, rgb_v)
    rgb[1]=(rgb_v, rgb_v, rgb_v)
    rgb[2]=(rgb_v, rgb_v, rgb_v)
    rgb.write()

    if(buzz_v == 0):
      music.stop()
    else:
      music.pitch(1000,500)
  except:
    oled.DispChar(msg,0,0)
    oled.show()