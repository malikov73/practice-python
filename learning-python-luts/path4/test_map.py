from functools import reduce
import random


def sortS(x, y): return x if x+5 > y else False


tmp_list1 = [random.randint(1, i) for i in range(2, 50)]
tmp_list2 = [random.randint(1, i) for i in range(2, 50)]
print(list(map(sortS, tmp_list1, tmp_list2)))

tmp_file = [x for x in open("file.txt")]
print("file list ", tmp_file)
