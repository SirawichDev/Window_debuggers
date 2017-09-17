from ctypes import *

libc = cdll.msvcrt
print(libc)
msg_str = "Hello miew~\n"
libc.printf("Testing: %s",msg_str)
