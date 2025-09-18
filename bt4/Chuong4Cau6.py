'''
Những giá trị nào có thể xuất hiện trong randrange(0, 100)
'''
from random import randrange
import random
values = set()
while len(values) < 100:
    values.add(random.randrange(0, 100))
print(sorted(values))