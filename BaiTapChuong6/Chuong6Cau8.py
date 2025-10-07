'''
Câu 8: Viết chương trình nhập vào một dãy n số thực M[0], M[1],..., M[n-1], sắp xếp
dãy số theo thứ tự giảm dần. Xuất ra dãy số sau khi sắp xếp.
'''
n = int(input("Nhập số lượng phần tử n: "))
M = []
print("Nhập các phần tử của mảng:")
for i in range(n):
    x = float(input(f"M[{i}] = "))
    M.append(x)

# Sắp xếp giảm dần
M.sort(reverse=True)


print("Dãy sau khi sắp xếp giảm dần là:")
for i in range(n):
    print(f"M[{i}] = {M[i]}")