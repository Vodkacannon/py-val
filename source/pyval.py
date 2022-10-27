def eval_expression_of_x(expression: str) -> float: 
    # Block due to presence of some special characters.
    if any(sub_chr in [":", "="] for sub_chr in expression):
        return None
	
    # Block non-'x' letters.
    elif any((char.isalpha() || char != 'x') for char in expression):
        return None
		
    # Block due to operator absence.
    elif not any(sub_str in ["+", "-", "*", "/", "%", "//", "**"] for sub_str in expression):
        return None

    # Everything should be securely parsed.
    try:
        return eval(expression)
    except:
        raise ArithmeticError("Invalid expression.")

	
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

	
# Eval Integral.
'''
Float based iterator.
'''
def float_range(start: float, stop: float, increment: float) -> float:
    while start < stop:
        yield start
        start += increment


def riemann_sum_partial(python_expression: str, x: float, infinitesimal) -> float:
    return eval_expression_of_x(python_expression) * infinitesimal


'''
Using a Riemann sum.
'''
def integrate(python_expression: str, low: float, high: float, infinitesimal: float = 0.001) -> float:
    return sum(riemann_sum_partial(python_expression, x, infinitesimal) for x in float_range(low, high, infinitesimal))
