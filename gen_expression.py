from asteval import Interpreter
import numpy as np

aeval = Interpreter()

np.random.seed(8746345)

def gen_expression():
    """Returns a string of a mathematical expression generated at random"""

    pass

for k,v in aeval.symtable.items():
    if callable(v):
        print(f'{k} : {v}\n')
        