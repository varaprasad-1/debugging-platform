import random
from algorithm_templates import TEMPLATES
from mutator import mutate_code
from bug_injector import inject_bug


# stores already generated programs
generated_codes = set()


def generate_bug():

    while True:

        # 1️⃣ pick random template
        template = random.choice(TEMPLATES)

        # 2️⃣ mutate variables / constants
        mutated_code = mutate_code(template)

        # 3️⃣ inject a bug
        buggy_code, fix = inject_bug(mutated_code)

        # 4️⃣ ensure bug exists
        if buggy_code is None:
            continue

        # 5️⃣ prevent duplicates
        if buggy_code in generated_codes:
            continue

        generated_codes.add(buggy_code)

        # 6️⃣ description
        description = "Fix the bug in the following program."

        return description, buggy_code, fix
