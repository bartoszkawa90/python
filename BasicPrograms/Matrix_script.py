#!/bin/python3

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)


letters = [ele[i] for i in range(3) for ele in matrix]
decoded_matrix = ''.join(letters)
decoded_matrix_without_non_alfanumeric_signs = re.sub('[^0-9a-zA-Z]', ' ', decoded_matrix)
clean_decoded_matrix = re.sub(' +', ' ', decoded_matrix_without_non_alfanumeric_signs)
print(clean_decoded_matrix)