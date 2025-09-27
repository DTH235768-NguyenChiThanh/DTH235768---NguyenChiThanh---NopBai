'''
Câu 7: Tối ưu chuỗi danh từ
'''
def ToiUuChuoiDanhTu(s: str):
    words = s.strip().split()
    words = [word.capitalize() for word in words if word]
    return ' '.join(words)
#ví dụ
input_str = "  nGUYỄN    chÍ   thANH  "
output_str = ToiUuChuoiDanhTu(input_str)    
print(output_str)