'''Chuong2Cau10 - ví dụ các phép gán rút gọn trong Python

Mỗi mục (a)-(g) hiển thị biểu thức gốc dưới dạng comment
và thực hiện biểu thức tương đương bằng toán tử gán rút gọn.
'''

def demo():
	x = 10
	y = 3
	ncc = 4
	number_of_closed_cases = 7

	# (a) x = x + 1  -> x += 1
	x = 10
	x += 1
	print("(a) x += 1 ->", x)

	# (b) x = x / 2  -> x /= 2
	x = 10
	x /= 2
	print("(b) x /= 2 ->", x)

	# (c) x = x - 1  -> x -= 1
	x = 10
	x -= 1
	print("(c) x -= 1 ->", x)

	# (d) x = x + y  -> x += y
	x = 10
	x += y
	print("(d) x += y ->", x)

	# (e) x = x - (y + 7)  -> x -= (y + 7)
	x = 20
	x -= (y + 7)
	print("(e) x -= (y + 7) ->", x)

	# (f) x = 2*x  -> x *= 2
	x = 6
	x *= 2
	print("(f) x *= 2 ->", x)

	# (g) number_of_closed_cases = number_of_closed_cases + 2*ncc
	#     -> number_of_closed_cases += 2*ncc
	number_of_closed_cases = 7
	number_of_closed_cases += 2 * ncc
	print("(g) number_of_closed_cases += 2*ncc ->", number_of_closed_cases)


if __name__ == '__main__':
	demo()

