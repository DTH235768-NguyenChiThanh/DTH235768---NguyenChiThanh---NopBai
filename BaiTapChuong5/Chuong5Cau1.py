'''
Câu 1: Kiểm tra chuỗi đối xứng
'''
def CheckDoiXung(s):
    flag = True
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            flag = False
            break
    return flag
def main():
    print("Nhap 1 chuoi:")
    s = input()
    if(CheckDoiXung(s)):
        print("Chuoi ban da nhap doi xung<>")
    else:
        print("Chuoi ban da nhap khong doi xung<>")
while True:
    main()
    print("Tiep ko Thim Ba?")
    s = input()
    if s == 'k':
        break
print("Cam on Thim Ba!")
