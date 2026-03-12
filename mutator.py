import random
import re

VAR_NAMES = ["sum", "total", "result", "value"]
COUNT_NAMES = ["count", "cnt", "counter"]
ARRAY_NAMES = ["arr", "data", "nums", "values"]
INDEX_NAMES = ["i", "j", "k"]

def replace_word(code, old, new):
    return re.sub(r"\b" + old + r"\b", new, code)

def mutate_variables(code):

    code = replace_word(code, "i", random.choice(INDEX_NAMES))
    code = replace_word(code, "arr", random.choice(ARRAY_NAMES))
    code = replace_word(code, "sum", random.choice(VAR_NAMES))
    code = replace_word(code, "count", random.choice(COUNT_NAMES))

    return code

def mutate_code(code):

    code = mutate_variables(code)

    return code
