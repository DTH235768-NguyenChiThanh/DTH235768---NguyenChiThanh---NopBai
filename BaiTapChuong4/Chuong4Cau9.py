'''
Viết chương trình tính căn bậc 2 lồng nhau
'''
import math
x = float(input("Nhập số x để tính căn bậc 2 lồng nhau (x >= 0): "))

if x >= 0:
    result = math.sqrt(math.sqrt(x))
    print(f"Căn bậc 2 lồng nhau của {x} là: {result}")
else:
    print("Giá trị nhập vào không hợp lệ. Yêu cầu x >= 0.")