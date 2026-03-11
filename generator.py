import random
from algorithm_templates import TEMPLATES
from bug_injector import inject_bug
from mutator import mutate_code

# copy templates so we can remove used ones
available_templates = TEMPLATES.copy()

# avoid duplicate programs
generated = set()


def generate_bug():

    global available_templates

    # stop when all templates used
    if not available_templates:
        return (
            "All debugging challenges have been used.",
            "No more challenges available.",
            ""
        )

    while True:

        template = random.choice(available_templates)

        # remove template so logic never repeats
        available_templates.remove(template)

        # apply mutations
        template = mutate_code(template)

        # inject bug
        buggy_code, fix = inject_bug(template)

        if buggy_code and buggy_code not in generated:

            generated.add(buggy_code)

            description = """
Fix the bug in the following C program.
"""

            return description, buggy_code, fix
