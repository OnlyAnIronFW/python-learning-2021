import serial
ser = serial.Serial()
ser.baudrate=115200
ser.port='COM7'
ser.open()
while True:
    print(ser.readline())
