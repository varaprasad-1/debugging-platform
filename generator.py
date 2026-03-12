import random
from algorithm_templates import TEMPLATES
from bug_injector import inject_bug
from mutator import mutate_code

generated_codes = set()

descriptions = [
"Fix the bug in the following program.",
"Debug the following algorithm.",
"Identify and correct the error.",
"Correct the logical mistake in the code."
]


def generate_bug():

    while True:

        template = random.choice(TEMPLATES)

        code = template

        code = mutate_code(code)

        buggy_code, fix = inject_bug(code)

        if buggy_code and buggy_code not in generated_codes:

            generated_codes.add(buggy_code)

            description = random.choice(descriptions)

            return description, buggy_code, fix
