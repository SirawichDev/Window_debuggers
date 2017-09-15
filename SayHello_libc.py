from ctypes import *

libc = cdll("libc.so.6")
msg_str = "Hello miew~"
libc.printf("Testing: %s",msg_str)
