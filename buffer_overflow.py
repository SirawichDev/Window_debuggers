from ctypes import *

msvcrt = cdll.msvcrt

input("Press any key.")

#Create 8-byte destination Buffer
Buff = c_char_p("AA")

#The overflow string

overflow = "A" * 100

msvcrt.strcpy(Buff, overflow)

os.environ(Buff, overflow)
