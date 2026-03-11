import random
from algorithm_templates import TEMPLATES
from bug_injector import inject_bug

generated=set()

def generate_bug():

    while True:

        template=random.choice(TEMPLATES)

        buggy_code,fix=inject_bug(template)

        if buggy_code and buggy_code not in generated:

            generated.add(buggy_code)

            return buggy_code,fix