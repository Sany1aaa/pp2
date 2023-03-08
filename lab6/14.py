
import math
import time

num = int(input())
wait = int(input())
time.sleep(wait / 1000)
print(f"Square root of {num} after {wait} miliseconds is {math.sqrt(num)}")
