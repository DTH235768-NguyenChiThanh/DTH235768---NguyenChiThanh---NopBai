'''Đếm các loại ký tự trong chuỗi, sử dụng các hàm cơ bản.
Viết chương trình cho phép nhập vào 1 chuỗi. Yêu cầu xuất ra:
- Bao nhiêu chữ IN HOA
- Bao nhiêu chữ in thường
- Bao nhiêu chữ là chữ số
- Bao nhiêu chữ là ký tự đặc biệt
- Bao nhiêu chữ là khoảng trắng
- Bao nhiêu chữ là Nguyên Âm
- Bao nhiêu chữ là Phụ âm
'''




def is_vowel(ch):
    return ch.lower() in 'aeiou'

def count_upper(s):
    return sum(1 for c in s if 'A' <= c <= 'Z')

def count_lower(s):
    return sum(1 for c in s if 'a' <= c <= 'z')

def count_digits(s):
    return sum(1 for c in s if '0' <= c <= '9')

def count_spaces(s):
    return sum(1 for c in s if c.isspace())

def count_special(s):
    return sum(1 for c in s if not (c.isalpha() or c.isdigit() or c.isspace()))

def count_vowels(s):
    return sum(1 for c in s if c.isalpha() and is_vowel(c))

def count_consonants(s):
    return sum(1 for c in s if c.isalpha() and not is_vowel(c))


def main():
    s = input('Nhập chuỗi: ')
    print('In hoa:', count_upper(s))
    print('In thường:', count_lower(s))
    print('Chữ số:', count_digits(s))
    print('Ký tự đặc biệt:', count_special(s))
    print('Khoảng trắng:', count_spaces(s))
    print('Nguyên âm:', count_vowels(s))
    print('Phụ âm:', count_consonants(s))

if __name__ == '__main__':
    main()


