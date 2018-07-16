"""
s = "123"
sum = 0
S = []
for i in s:
    print(ord(i), end="|")
    sum += ord(i)
    S.append(ord(i))
print(sum)
print(S)
print(list(map(ord, s)))
"""
import random

dict = {}
for i in range(9):
    dict[random.randint(0, 100)] = i

print(sorted(list(dict.keys())))

test_list = []
for i in range(30):
    test_list.append(random.randint(1, 1000))
test_list.sort()
print(test_list)
