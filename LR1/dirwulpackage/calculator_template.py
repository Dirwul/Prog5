import math

__all__ = ['evaluate_expression', 'parse_expression']

# Функция, вычисляющая значение выражения
def evaluate_expression(expression):
    try:
        return eval(expression, {"__builtins__": None}, {"math": math})
    except Exception as e:
        return str(e)

# Функция, разбивающая выражение на операторы и операнды
def parse_expression(expression):
    operators = {'+', '-', '*', '/', '^'}
    parsed_expression = []
    current_token = ''

    for char in expression:
        if char.isdigit() or char == '.':
            current_token += char
        elif char in operators:
            if current_token:
                parsed_expression.append(float(current_token))
                current_token = ''
            parsed_expression.append(char)
        elif char == ' ':
            continue
        else:
            raise ValueError("Invalid character: " + char)

    if current_token:
        parsed_expression.append(float(current_token))

    return parsed_expression