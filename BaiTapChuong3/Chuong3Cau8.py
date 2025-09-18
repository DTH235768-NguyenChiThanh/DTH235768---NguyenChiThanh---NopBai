'''
Nhập vào 2 giá trị a, b và phép toán ‘+’, ‘-’, ‘*’, ‘/’ . Hãy xuất kết quả theo
đúng phép toán đã nhập.
'''
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
ch = (input("Nhập toán tử (+, -, *, /): "))
if ch == "+":
    kq = a + b
    print(kq)
    n = 1
elif ch == "-":
    kq = a - b
    print(kq)
    n = 1
elif ch == "*":
    kq = a * b
    print(kq)
    n =1
elif ch == "/":
    kq = a / b
    print(kq)
    n = 1
else:
    print("kí tự", ch, "ko phải là toán tử!")