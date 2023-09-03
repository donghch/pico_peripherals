"""
Pico Lcd1602 Library written by henrydhc
Date: Sep 02 2023
"""

#Library Imports
from machine import Pin
from time import sleep_us
from time import sleep_ms

#Instruction Definitions
LCD1602_CLEAR = 0x1
LCD1602_RETURN_HOME = 0x2

#Char Definitions
chars = {"0": 0x30, "1": 0x31, "2": 0x32, "3": 0x33, "4": 0x34,
         "5": 0x35, "6": 0x36, "7": 0x37, "8": 0x38, "9": 0x39,
         "A": 0x41, "B": 0x42, "C": 0x43, "D": 0x44, "E": 0x45,
         "F": 0x46, "G": 0x47, "H": 0x48, "I": 0x49, "J": 0x4a,
         "K": 0x4b, "L": 0x4c, "M": 0x4d, "N": 0x4e, "O": 0x4f,
         "P": 0x50, "Q": 0x51, "R": 0x52, "S": 0x53, "T": 0x54,
         "U": 0x55, "V": 0x56, "W": 0x57, "X": 0x58, "Y": 0x59,
         "Z": 0x5a, "a": 0x61, "b": 0x62, "c": 0x63, "d": 0x64,
         "e": 0x65, "f": 0x66, "g": 0x67, "h": 0x68, "i": 0x69,
         "j": 0x6a, "k": 0x6b, "l": 0x6c, "m": 0x6d, "n": 0x6e,
         "o": 0x6f, "p": 0x70, "q": 0x71, "r": 0x72, "s": 0x73,
         "t": 0x74, "u": 0x75, "v": 0x76, "w": 0x77, "x": 0x78,
         "y": 0x79, "z": 0x7a, "!": 0x21, "\"": 0x22, "#": 0x23,
         "$": 0x24, "%": 0x25, "&": 0x26, "\'": 0x27, "(": 0x28,
         ")": 0x29, "*": 0x2a, "+": 0x2b, ",": 0x2c, "-": 0x2d,
         ".": 0x2e, "/": 0x2f
         }



class LCD1602:
    
    def __init__(self, pin_rs: int, pin_rw: int, pin_enable: int,
                 pin_db0: int, pin_db1: int, pin_db2: int, pin_db3: int,
                 pin_db4: int, pin_db5: int, pin_db6: int, pin_db7: int):
        #Init Pins
        self.rs = Pin(pin_rs, Pin.OUT)
        self.rw = Pin(pin_rw, Pin.OUT)
        self.en = Pin(pin_enable, Pin.OUT)
        self.dbs = list()
        self.dbs.append(Pin(pin_db0, Pin.OUT))
        self.dbs.append(Pin(pin_db1, Pin.OUT))
        self.dbs.append(Pin(pin_db2, Pin.OUT))
        self.dbs.append(Pin(pin_db3, Pin.OUT))
        self.dbs.append(Pin(pin_db4, Pin.OUT))
        self.dbs.append(Pin(pin_db5, Pin.OUT))
        self.dbs.append(Pin(pin_db6, Pin.OUT))
        self.dbs.append(Pin(pin_db7, Pin.OUT))
        
        
    def write_data(self, data):
        sleep_us(5)
        self.rs.value(1)
        self.rw.value(0)
        self.en.value(1)
        for i in range(0, 8):
            self.dbs[i].value((data >> i) & 0x1)
        sleep_us(5)
        self.en.value(0)
        sleep_us(5)
        self.rw.value(1)
    
    def write_command(self, cmd):
        sleep_us(5)
        self.rs.value(0)
        self.rw.value(0)
        self.en.value(1)
        for i in range(0, 8):
            self.dbs[i].value((cmd >> i) & 0x1)
        sleep_us(5)
        self.en.value(0)
        sleep_us(5)
        self.rw.value(1)
    
    def print_str(data: str):
        pass
    
    def reset(self):
        self.write_command(LCD1602_CLEAR)
        sleep_ms(2)
    
    def move_cursor():
        pass
    
    def set_function(self):
        pass