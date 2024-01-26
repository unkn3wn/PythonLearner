# input output using python sys
import sys

for line in sys.stdin:
    if "q" == line.rstrip():
        break
    print(f"Input: {line}")

print("exit")