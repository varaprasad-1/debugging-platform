import random
import re

# possible replacements
VAR_NAMES = ["sum", "total", "result", "value"]
COUNT_NAMES = ["count", "cnt", "counter"]
ARRAY_NAMES = ["arr", "data", "nums", "values"]
INDEX_NAMES = ["i", "j", "k"]

def replace_word(code, old, new):
    return re.sub(r"\b" + old + r"\b", new, code)


def mutate_variables(code):

    # mutate index variables
    new_index = random.choice(INDEX_NAMES)
    code = replace_word(code, "i", new_index)

    # mutate array name
    new_array = random.choice(ARRAY_NAMES)
    code = replace_word(code, "arr", new_array)

    # mutate sum variable
    new_sum = random.choice(VAR_NAMES)
    code = replace_word(code, "sum", new_sum)

    # mutate count variable
    new_count = random.choice(COUNT_NAMES)
    code = replace_word(code, "count", new_count)

    return code


def mutate_constants(code):

    # replace constant numbers with random values
    constants = ["10", "2", "3", "5"]

    for c in constants:
        if c in code:
            code = code.replace(c, str(random.randint(2, 15)))

    return code


def mutate_code(code):

    code = mutate_variables(code)
    code = mutate_constants(code)

    return code