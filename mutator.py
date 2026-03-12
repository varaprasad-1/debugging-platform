import random
import re

# possible variable replacements
VAR_NAMES = ["sum", "total", "result", "value"]
ARRAY_NAMES = ["arr", "data", "nums", "values"]
INDEX_NAMES = ["i", "j", "k"]

# constants that may appear in templates
CONSTANTS = [2, 3, 4, 5, 7, 10]


def replace_word(code, old, new):
    return re.sub(r"\b" + old + r"\b", new, code)


def mutate_variables(code):

    code = replace_word(code, "arr", random.choice(ARRAY_NAMES))
    code = replace_word(code, "sum", random.choice(VAR_NAMES))
    code = replace_word(code, "count", random.choice(VAR_NAMES))
    code = replace_word(code, "i", random.choice(INDEX_NAMES))

    return code


def mutate_constants(code):

    for c in CONSTANTS:
        code = re.sub(
            r"\b" + str(c) + r"\b",
            str(random.randint(2, 15)),
            code
        )

    return code


def mutate_code(code):

    code = mutate_variables(code)
    code = mutate_constants(code)

    return code
