import pyval as pv

print(pv.eval_arithmetic(""))
print(pv.eval_arithmetic("42"))
print(pv.eval_arithmetic("(((1 + 2 + 3 - 6) / (4 * 5))**2.5"))
print(pv.eval_arithmetic("print('Some malicious code.'"))

print(pv.eval_expression_of_x(3.14159), "x * r**2")
print(pv.differentiate("x**2"), 3.14159, 0.00001)