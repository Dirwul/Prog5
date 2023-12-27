from LR1.dirwulpackage.calculator import *
from LR1.dirwulpackage.calculator_template import *

__all__ = calculator.__all__ + calculator_template.__all__

def hello(name):
    print('This is __init__.py hello function')
    print(f"Hello, {name}")