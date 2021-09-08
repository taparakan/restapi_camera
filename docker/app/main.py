import serial

from typing import Optional

from fastapi import FastAPI

app = FastAPI()

arduino = serial.Serial(port='/dev/ttyACM0', baudrate=38400, timeout=.1)

def write_to_arduino(msg):
    arduino.write(bytes(msg,'utf-8'))

@app.get("/")
def read_root():
    return {"Hejo": "Swiecie"}

app.licznik = 0

@app.get("/licz")
def licznik():
    app.licznik = app.licznik + 1
    return {"wartosc" : app.licznik}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/s1/{degree}")
def move_s1_left(degree: int):
    write_to_arduino(f's1:{degree}\n')
    return f'Obrocono o kat {degree} stopni' 

@app.get("/s2/left")
def move_s1_left():
    write_to_arduino("s2:l\n")
    return "Sent"

@app.get("/s2/right")
def move_s1_right():
    write_to_arduino("s2:r\n")
    return "Sent"

