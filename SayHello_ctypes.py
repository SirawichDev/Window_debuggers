from ctypes import *

libc = CDLL("libc.dylib")
msg = "Hello Miew"
libc.printf("TEST : %s",msg)