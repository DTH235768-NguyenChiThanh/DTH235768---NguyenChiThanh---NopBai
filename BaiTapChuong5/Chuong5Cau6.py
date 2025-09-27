'''Câu 6: Trích lọc số âm trong chuỗi
'''
import re 
def NegativeNumberInStrings(s: str):
    # Tìm tất cả số nguyên có dấu âm trong chuỗi
    numbers = re.findall(r'-(\d+)', s)
    # Chuyển các chuỗi số thành số nguyên âm 
    negative_numbers = [-int(num) for num in numbers]
    return negative_numbers
# Ví dụ chạy thử
s = "abc-5xyz-12k9l--p"
print(NegativeNumberInStrings(s))