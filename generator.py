import random
from algorithm_templates import TEMPLATES
from bug_injector import inject_bug
from mutator import mutate_code

def generate_bug():
    while True:
        template = random.choice(TEMPLATES)
        description = template["description"]
        code = template["code"]
        
        # Mutate the original code template
        code = mutate_code(code)
        
        # Inject a bug and return the result if successful
        buggy_code, fix = inject_bug(code)
        if buggy_code:
            return description, buggy_code, fix
