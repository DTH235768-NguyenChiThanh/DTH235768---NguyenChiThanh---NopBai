'''
Câu 9: Xử lý mảng
Trang 56/84
Yêu cầu:
Viết chương trình nhập vào một mảng số tự nhiên. Hãy xuất ra màn hình:
- Dòng 1 : gồm các số lẻ, tổng cộng có bao nhiêu số lẻ.
- Dòng 2 : gồm các số chẵn, tổng cộng có bao nhiêu số chẵn.
- Dòng 3 : gồm các số nguyên tố.
- Dòng 4 : gồm các số không phải là số nguyên tố. 
'''
n = int(input("Nhập số phần tử: "))
lst = []

for i in range(n):
    x = int(input(f"Nhập phằn tử thứ {i+1}:"))
    lst.append(x)

def SoLe(x):
    if x % 2 == 0:
        return False
    return True
tamle = []
demle = 0
tamchan = []
demchan = 0
for i in range(n):
    demle += 1
    tamle.append(lst[i])
else:
    demchan += 1
    tamchan.append(lst[i])
print("Danh sách số lẻ là: ")
print(tamle)
print("Có", demle, " số lẻ trong List.")

print("Danh sách số chẵn là: ")
print(tamchan)
print("Có", demchan, " số chẵn trong List.")

def CheckPrime(n):
    d = 0
    for i in range(1, n+1):
        if n % i == 0:
            d += 1
    return d == 2

demnt == 0
tamnt = []
demknt = 0
tamknt = []
for i in range(n):
    if CheckPrime(lst[i]):
        demnt += 1
        tamnt.append(lst[i])
    else:
        demknt += 1
        tamknt.append(lst[i])
print("Danh sách số nguyên tố là: ")
print(tamnt)
print("Có", demnt, " số nguyên tố trong List.")

print("Danh sách ko phải số nguyên tố là: ")
print(tamknt)
print("Có", demknt, "số ko phải là số nguyên tố")

print("Danh sách vừa nhập là: ")
print(lst)
