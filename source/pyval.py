def eval_math(expression: str):
    # Block due to numeric absence.
    if not any(char.isdigit() for char in expression):
        return 0
    
    # Block due to presence of some special characters.
    elif any(sub_chr in [":", "="] for sub_chr in expression):
        return 0
	
    # Block letters (upper and lower case).
    elif any(char.isalpha() for char in expression):
        return 0
		
    # Block due to operator absence.
    elif not any(sub_str in ["+", "-", "*", "/", "%", "//", "**"] for sub_str in expression):
        return 0

    # Everything should be secure.
    try:
        return eval(expression)
    except:
        raise ArithmeticError("Invalid expression.")
