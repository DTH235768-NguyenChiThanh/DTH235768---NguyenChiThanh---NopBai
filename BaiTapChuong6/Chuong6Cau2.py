'''
Câu 2: Xử lý List nhập ngẫu nhiên
'''
from random import randrange
lst = []
print("Nhap so phan tu: ")
n = int(input())
for i in range(n):
    lst.append(randrange(0, 100))
print("List sau khi tao ngau nhien la: ")
print(lst)
x = int(input("Moi ban them so moi: "))
lst.append(x)
print("List sau khi them so moi la: ")
print(lst)
k = int(input("Thím muon xoa so nao: "))
while lst.count(k) > 0:
    lst.remove(k)
print("List sau khi xao la: ")
print(lst)

def CheckDoiXung(lst):
    for i in range(len[lst]):
        if lst[i] != lst[len(lst)-i-1]:
            return False
    return True
kt = CheckDoiXung(lst)
if kt == True:
    print("List doi xung")
else:
    print("List khong doi xung")