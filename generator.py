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

        # ❌ reject if no bug
        if not buggy_code or not fix:
            continue

        # ❌ reject if bug didn't change code
        if buggy_code == mutated:
            continue

        # ❌ reject duplicates
        if buggy_code in generated_codes:
            continue

        generated_codes.add(buggy_code)

        description = "Fix the bug in the following program."

        difficulty = random.choice(["Easy","Medium","Hard"])

        return description, buggy_code, fix, difficulty
