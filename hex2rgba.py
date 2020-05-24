#!usr/bin/python3
import sys

try:
    args = sys.argv[1]
except:
    print("XXX.py 607D8B")

Rhex = args[0:1]
Ghex = args[2:3]
Bhex = args[4:5]

R = int(Rhex,16)
G = int(Ghex,16)
B = int(Bhex,16)

res = f"{R/255:.2f},{G/255:.2f},{B/255:.2f},1"
print(res)
try:
    import pyperclip
    pyperclip.copy(res)
except ImportError:
    print("pyperclip install me! clickboard easy!")
