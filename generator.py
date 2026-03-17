import random
from algorithm_templates import TEMPLATES
from mutator import mutate_code
from bug_injector import inject_bug

def generate_bug():

    while True:

        template = random.choice(TEMPLATES)

        mutated = mutate_code(template)

        buggy_code, fix = inject_bug(mutated)

        # reject invalid
        if not buggy_code or not fix:
            continue

        if buggy_code == mutated:
            continue

        description = "Fix the bug in the following program."

        return description, buggy_code, fix