import random
from algorithm_templates import TEMPLATES
from mutator import mutate_code
from bug_injector import inject_bug

generated_codes = set()


def generate_bug():

    while True:

        template = random.choice(TEMPLATES)

        mutated = mutate_code(template)

        buggy_code, fix = inject_bug(mutated)

        if buggy_code and buggy_code not in generated_codes:

            generated_codes.add(buggy_code)

            description = "Fix the bug in the following program."

            return description, buggy_code, fix
