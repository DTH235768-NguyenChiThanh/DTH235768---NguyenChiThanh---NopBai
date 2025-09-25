'''
 Nhập vào một ngày (ngày, tháng, năm). Tìm ngày kế sau ngày
vừa nhập (ngày/tháng/năm)
'''
day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))

#xac dinh so ngay 
if month in [1,3,5,7,8,10,12]: 
    max_ngay = 31
elif month in [4,6,9,11]:
    max_ngay = 30
elif month == 2: 
    #kiem tra nam nhuan
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        max_ngay = 29
    else: 
        max_ngay = 28
else: 
    max_ngay = 0 #tháng sai 

#kiểm tra ngày hợp lệ 
if max_ngay == 0 or day < 1 or day > max_ngay:
    print("Ngày không hợp lệ!")
else: #tìm ngày kế tiếp
    day += 1
    if day > max_ngay: 
        day = 1
    
    print(f"Ngày kế tiếp là: {day}/{month}/{year}")