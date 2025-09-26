'''
Câu 1: Tính chu vi diện tích Hình tròn
'''
import math
try:
    r = float(input("Nhap ban kinh hinh tron: "))
    cv = 2 * math.pi * r
    dt = r ** 2
    print("Chu vi la: ", cv)
    print("Dien tich la: ", dt)
except:
    print("Nhap sai roi!")