'''
Tính và xuất độ dài đoạn AB
'''
import math

xA = float(input("Nhap hoanh do diem A (xA): "))
yA = float(input("Nhap tung do diem A (yA): "))

xB = float(input("Nhap hoanh do diem B (xB): "))
yB = float(input("Nhap tung do diem B (yB): "))

do_dai_AB = math.sqrt((xB - xA) **2 + (yB - yA) **2)
print(f"Do dai doan AB la: {do_dai_AB}")