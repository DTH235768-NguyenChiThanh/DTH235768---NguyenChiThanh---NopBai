'''
Viết Hàm tính BMI
'''
def BMI (height, weight):
    return weight/(height**2)
def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gay"
    elif bmi <= 24.9:
        return "Binh thuong"
    elif bmi <= 29.9:
        return "Hoi beo"
    elif bmi <= 34.9:
        return "Beo phi cap do 1"
    elif bmi <= 39.9:
        return "Beo phi cap do 2"
    else:
        return "beo phi cap do 3"
def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thap"
    elif bmi <= 24.9:
        return "Trung Binh"
    elif bmi <= 29.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rat cao"
    else:
        return "Nguy hiem"
print("Nhap cao chieu cao: ")
height = float(input())
print("Nhap vao can nang: ")
weight = float(input())
bmi = BMI(height, weight)
print("BMI cua ban: ", bmi)
print("Phan loai cua ban: ", PhanLoai(bmi))
print("Nguy co benh cua Thim la gi: ", NguyCoBenh(bmi))

    