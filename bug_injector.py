import random

BUG_PATTERNS = [

("i<n","i<=n"),           # off by one
("==","="),               # assignment bug
("arr[i]","arr[n]"),      # wrong index
("i++","i--"),            # infinite loop
("+=","="),               # wrong update
(">","<"),                # wrong condition
("*=","+="),              # wrong formula
("count++","count--")     # wrong update

]

def inject_bug(code):

    valid=[]

    for correct,bug in BUG_PATTERNS:
        if correct in code:
            valid.append((correct,bug))

    if not valid:
        return None,None

    correct,bug=random.choice(valid)

    buggy_code=code.replace(correct,bug,1)

    return buggy_code,correct