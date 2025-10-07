'''
Câu 6: Nhập vào 1 list có N số ngẫu nhiên KHÔNG TRÙNG NHAU
'''
from random import randrange
lst = []
print("Nhap so phan tu: ")
n = int(input())
while len(lst) < n:
    x = randrange(0, 150)
    if x not in lst:
        lst.append(x)
    else:
        continue
print("List sau khi tạo ngẫu nhiên ko trùng nhau là: ")
print(lst)