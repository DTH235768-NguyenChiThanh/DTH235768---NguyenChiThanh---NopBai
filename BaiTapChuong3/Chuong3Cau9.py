'''
 Nhập vào 1 tháng, xuất ra tháng đó thuộc quý mấy trong năm.
'''
Thang = int(input("Nhập tháng từ 1 -> 12: "))
if 1 <= Thang <= 3:
    print("Tháng", thang, "thuộc quý 1")
elif 4 <= Thang <= 6:
    print("Tháng", thang, "thuộc quý 2")
elif 7 <= Thang <= 9:
    print("Tháng", thang, "thuộc quý 3")
elif 10 <= Thang <= 12:
    print("Tháng", Thang, "thuộc quý 4")
else:
    print("Tháng ko hợp lệ nhá!")