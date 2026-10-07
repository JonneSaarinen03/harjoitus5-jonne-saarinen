from machine import Pin, PWM
from time import sleep

# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

def eteenpäin():
    m1.value(1) # moottorien pyörimis suunta
    m2.value(1)
    e1.duty_u16(33000) # oikean moottorin nopeus
    e2.duty_u16(33000) # vasemman moottorin nopeus
    sleep(4) # aika mitä ajetaan eteenpäin

def käännyoikealle():
    m1.value(0)
    m2.value(1)
    e1.duty_u16(33000)
    e2.duty_u16(33000)
    sleep(4)

def käännyvasemmalle():
    m1.value(1)
    m2.value(0)
    e1.duty_u16(33000)
    e2.duty_u16(33000)
    sleep(4)

def taaksepäin():
    m1.value(0)
    m2.value(0)
    e1.duty_u16(33000)
    e2.duty_u16(33000)
    sleep(4)

def käännyympäri():
    m1.value(0)
    m2.value(1)
    e1.duty_u16(33000)
    e2.duty_u16(33000)
    sleep(8)

def pysähdy():
    m1.value(1)
    m2.value(1)
    e1.duty_u16(0)
    e2.duty_u16(0)
    sleep(5)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# tauko
pysähdy()

# yrittää avata data tiedoston
try:
    with open("data.txt", "r") as tiedosto:
        # luetaan ohjeet data tiedostosta 
        for rivi in tiedosto:
            ohje = rivi.strip()

            
            if ohje == "eteenpäin":
                eteenpäin()

            elif ohje == "käännyoikealle":
                käännyoikealle()

            elif ohje == "käännyvasemmalle":
                käännyvasemmalle()

            elif ohje == "taaksepäin":
                taaksepäin()

            elif ohje == "käännyympäri":
                käännyympäri()

            elif ohje == "pysähdy":
                pysähdy()
# ilmoitetaan jos tulee virhe
except:
    print("virhe")


    