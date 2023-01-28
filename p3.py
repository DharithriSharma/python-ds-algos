
import numpy as np
a = np.array[1, 2, 3, 4]
b = np.array[5, 6, 7, 8]
c = np.array[2, 4, 6, 8]
add_ans_arth = a + b + c
print(add_ans_arth)
add_ans_mumpy = np.add(a, b, c)
print(add_ans_mumpy)
sub_ans_arth = a - b - c
print(sub_ans_arth)
sub_ans_numpy = np.subract(a, b, c)
print(sub_ans_numpy)
mul_ans_arth = a * b * c
print(mul_ans_arth)
mul_ans_numpy = np.multiply(a, b, c)
print(mul_ans_numpy)
div_ans_arth = a / b / c
print(div_ans_arth)
div_ans_numpy = np.divide(a, b, c)
print(div_ans_numpy)
rep = np.reciprocal(a)
rep = np.reciprocal(b)
rep = np.reciprocal(c)
