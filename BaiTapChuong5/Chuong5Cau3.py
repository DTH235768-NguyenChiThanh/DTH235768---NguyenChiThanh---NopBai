'''
Câu 3: Xử lý Tách chuỗi
'''
def CheckPrime(x):
    dem = 0
    for i in range(1, x +1):
        if x % i == 0:
            dem = dem + 1
    return dem == 2
s = "5;7;8;-2;8;11;-13;9;10"
arr = s.split(";")
sochan = 0
soam = 0
sont = 0
sum = 0
for x in arr:
    print(x)
    number = int(x)
    if number % 2 == 0:
        sochan += 1
    if number <= 0:
        soam += 1  
    if CheckPrime(number):
        sont = sont + 1
    sum = sum + number
print("So chan la: ", sochan)
print("So am la:", soam)
print("So nguyen to la: ", sont)
print("Trung binh la: ", sum/len(arr)) 