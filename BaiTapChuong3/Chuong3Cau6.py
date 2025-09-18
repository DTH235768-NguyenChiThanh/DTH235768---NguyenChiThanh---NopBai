'''
Nhập một số n có tối đa 2 chữ số. Hãy cho biết cách đọc ra dạng chữ.
(vd: n=35 => Ba mươi lăm, n=5 => năm)
'''
n  = int(input("Nhập số nguyên từ (-99 đến 99): "))
if -99 <= n <= 99: 
    so = ["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
    if n == 0:
        doc = "không"
    else: 
        am = n < 0
        n_abs = abs(n)

        if n_abs < 10: 
            doc = so[n_abs]
        else:
            chuc = n_abs//10
            donvi = n_abs % 10

            if chuc == 1: #10-19
                if donvi == 0:
                    doc = "mười"
                elif donvi == 15: 
                    doc = "mười lăm"
                else: 
                    doc = "mười" + so[donvi]
            else: #20 - 99
                doc = so[chuc] + " mươi"
                if donvi == 1: 
                    doc += " mốt"
                elif donvi == 5: 
                    doc += " lăm"
                elif donvi != 0: 
                    doc += " " + so[donvi]
        if n < 0: 
            doc = "âm " + doc
    
    print(f"Số đọc là: {doc}")
else: 
    print("Số không hợp lệ!")