import random
from algorithm_templates import TEMPLATES
from bug_injector import inject_bug
from mutator import mutate_code


def generate_bug():

    while True:

        template = random.choice(TEMPLATES)

        # simple description generator
        description = "Debug the following program."

        code = template

        # mutate variables to create variety
        code = mutate_code(code)

        # inject bug
        buggy_code, fix = inject_bug(code)

        # ensure valid bug was inserted
        if buggy_code:
            return description, buggy_code, fix
