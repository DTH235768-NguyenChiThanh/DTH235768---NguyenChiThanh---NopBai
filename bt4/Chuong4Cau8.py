'''
Viết chương trình tính loga
x
'''
import math

a = float(input("Nhập cơ số a (a > 0, a != 1): "))
x = float(input("Nhập số x (x > 0): "))

if a > 0 and a != 1 and x > 0:
    loga_x = math.log(x) / math.log(a)
    print(f"log_{a}({x}) = {loga_x}")
else:
    print("Giá trị nhập vào không hợp lệ. Yêu cầu a > 0, a != 1, x > 0.")