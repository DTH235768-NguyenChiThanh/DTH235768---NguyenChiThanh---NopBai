'''
 Viết Hàm để chơi Game Đoán Số
'''
from random import randrange
while True:
    somay = randrange(1,101)
    solandoan = 0
    win = False
    while solandoan < 7:
        solandoan += 1
        songuoi = int(input("may doan [1..10], moi ban doan: "))
        print("Ban doan lan thu ", solandoan)
        if somay == songuoi:
            print("Chuc mung ban doan dung, so may la: ", somay)
            win = True
            break
        if somay > songuoi:
            print("Ban doan sai, so may > so ban")
        elif somay < songuoi:
            print("Ban doan sai, so may < so ban")
    if win == False:
        print("GAME OVER!, so may: ", somay)
    hoi = input("Tiep khong?")
    if hoi == "k":
        break
print("Cam on ban da choi game!")