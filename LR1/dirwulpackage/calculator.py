from LR1.dirwulpackage.calculator_template import *

__all__ = ['calculate']

# Функция, выполняющая cвычисление сложного выражения
def calculate(expression):
    parsed_expression = parse_expression(expression)
    result = parsed_expression[0]

    for i in range(1, len(parsed_expression), 2):
        operator = parsed_expression[i]
        operand = parsed_expression[i + 1]

        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            result /= operand
        elif operator == '^':
            result **= operand

    return result