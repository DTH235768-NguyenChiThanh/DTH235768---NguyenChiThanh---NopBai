'''
Hàm oscillate

'''
def oscillate(a, b):
    
        # xác định dấu của a (nếu a == 0 thì coi là dương)
        s = 1 if a >= 0 else -1
        m = min(abs(a), abs(b))

        # phần giảm dần (từ m về 0), mỗi bước in hai giá trị: s*k rồi -s*k
        for k in range(m, -1, -1):
                yield s * k
                yield -s * k

        # phần tăng dần trở lại (từ 1 tới m), in ngược chiều so với trên
        for k in range(1, m + 1):
                yield -s * k
                yield s * k
