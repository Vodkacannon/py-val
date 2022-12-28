'''
Algebraic.
'''
def eval_expression_of_x(expression: str, x: float) -> float: 
    # Block due to presence of some special characters.
    if any(sub_chr in [":", "="] for sub_chr in expression):
        return None
	
    # Block non-'x' letters.
    elif any((char.isalpha() or char != 'x') for char in expression):
        return None
		
    # Block due to operator absence.
    elif not any(sub_str in ["+", "-", "*", "/", "%", "//", "**"] for sub_str in expression):
        return None

    # Everything should be securely parsed.
    try:
        return eval(expression)
    except:
        raise ArithmeticError("Invalid expression.")

'''
Non algebraic.
'''
def eval_arithmetic(expression: str) -> float:
    # Block due to numeric absence.
    if not any(char.isdigit() for char in expression):
        return None
    
    # Block due to presence of some special characters.
    elif any(sub_chr in [":", "="] for sub_chr in expression):
        return None
	
    # Block letters (upper and lower case).
    elif any(char.isalpha() for char in expression):
        return None
		
    # Block due to operator absence.
    elif not any(sub_str in ["+", "-", "*", "/", "%", "//", "**"] for sub_str in expression):
        return None

    # Everything should be securely parsed.
    try:
        return eval(expression)
    except:
        raise ArithmeticError("Invalid arithmetic.")

	


'''
A single variable differentiator.
'''
def differentiate(python_expression: str, x: float, infinitesimal: float = 0.001) -> float:
    x += infinitesimal
    f_of_x_plus_h = eval(python_expression)

    x -= infinitesimal
    f_of_x = eval(python_expression)
    
    return (f_of_x_plus_h - f_of_x) / infinitesimal


'''
A single variable second order differentiator.
'''
def differentiate_second_order(python_expression: str, x: float, infinitesimal: float = 0.001) -> float:
    x += infinitesimal
    f_of_x_plus_h = eval(python_expression)
    
    x -= infinitesimal
    f_of_x = eval(python_expression)
    
    two_times_f_of_x = 2.0 * f_of_x

    x -= infinitesimal
    f_of_x_minus_h = eval(python_expression)

    return (f_of_x_plus_h - two_times_f_of_x + f_of_x_minus_h) / infinitesimal ** 2


'''
Find the curvature of a function of a single variable.
'''
def curvature(python_expression: str, x: float, infinitesimal: float = 0.001) -> float:
    numerator = abs(differentiate_second_order(python_expression, x, infinitesimal))
    denominator = (1.0 + differentiate(python_expression, x, infinitesimal) ** 2) ** 1.5
    return numerator / denominator


'''
Float based iterator.
'''
def float_range(start: float, stop: float, increment: float) -> float:
    while start < stop:
        yield start
        start += increment


def riemann_sum_partial(python_expression: str, x: float, infinitesimal: float) -> float:
    return eval_expression_of_x(python_expression, x) * infinitesimal


'''
# Eval integral using a Riemann sum.
'''
def integrate(python_expression: str, low: float, high: float, infinitesimal: float = 0.001) -> float:
    return sum(riemann_sum_partial(python_expression, x, infinitesimal) for x in float_range(low, high, infinitesimal))
