import tkinter as tk
import serial
import json

window=tk.Tk()
window.title('控制掌控LED灯及蜂鸣器')
window.geometry('200x200')
com=serial.Serial('COM7',115200,timeout=2) #更改成你自己的串口号

l=tk.Label(window,width=40,height=4,text='控制掌控板的LED灯及蜂鸣器')
l.pack()

rgb=0
buzz=0

def send_command():
  global rgb,buzz
  msg={}
  msg["rgb"]=rgb
  msg["buzz"]=buzz
  print(json.dumps(msg))
  com.write((json.dumps(msg)+"\r\n").encode('utf-8'))

def rgb_onoff():
  global rgb
  if rgb_btn_onoff['text'] == u"打开LED灯":
    rgb_btn_onoff['text'] = u"关闭LED灯"
    rgb = 255
  else:
    rgb_btn_onoff['text'] = u"打开LED灯"
    rgb = 0
  send_command()

def buzz_onoff():
  global buzz
  if buzz_btn_onoff['text'] == u"打开蜂鸣器":
    buzz_btn_onoff['text'] = u"关闭蜂鸣器"
    buzz = 1
  else:
    buzz_btn_onoff['text'] =  u"打开蜂鸣器"
    buzz = 0
  send_command()

rgb_btn_onoff = tk.Button(window, text=u"打开LED灯", command=rgb_onoff)
rgb_btn_onoff.place(x=50, y=60, width=100, height=40)

buzz_btn_onoff = tk.Button(window, text=u"打开蜂鸣器", command=buzz_onoff)
buzz_btn_onoff.place(x=50, y=120, width=100, height=40)

window.mainloop()
