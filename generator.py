import random
from algorithm_templates import TEMPLATES
from bug_injector import inject_bug
from mutator import mutate_code


def generate_bug():

    while True:

        template = random.choice(TEMPLATES)

        # Handle both dictionary templates and string templates
        if isinstance(template, dict):
            description = template.get("description", "Fix the bug in the following code.")
            code = template.get("code", "")
        else:
            description = "Fix the bug in the following program."
            code = template

        # Apply mutation
        code = mutate_code(code)

        # Inject bug
        buggy_code, fix = inject_bug(code)

        # Ensure a bug was actually inserted
        if buggy_code:
            return description, buggy_code, fix
