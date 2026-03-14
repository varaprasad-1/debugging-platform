import random
from algorithm_templates import TEMPLATES
from mutator import mutate_code
from bug_injector import inject_bug

generated_codes = set()

DIFFICULTY_LEVELS = ["Easy", "Medium", "Hard"]

def generate_bug():

    while True:

        template = random.choice(TEMPLATES)

        mutated = mutate_code(template)

        buggy_code, fix = inject_bug(mutated)

        if buggy_code is None:
            continue

        if buggy_code in generated_codes:
            continue

        generated_codes.add(buggy_code)

        description = "Fix the bug in the following program."

        difficulty = random.choice(DIFFICULTY_LEVELS)

        return description, buggy_code, fix, difficulty
