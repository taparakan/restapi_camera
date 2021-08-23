# Importing Libraries
import serial
import time
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=38400, timeout=0.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))

while True:
    num = input("Enter a message: ") # Taking input from user
    write_read(num)
