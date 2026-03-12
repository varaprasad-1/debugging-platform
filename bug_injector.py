import random

BUG_PATTERNS = [

("i<n", "i<=n"),
("i<n", "i<n-1"),
("i<=n", "i<n"),

("==", "="),
(">", "<"),
("<", ">"),

("arr[i]", "arr[n]"),
("arr[i]", "arr[i+1]"),

("+=", "-="),
("*=", "+="),

("sum=0", "sum=1"),
("count=0", "count=1"),

("i++", "i--"),
("count++", "count--")

]


def inject_bug(code):

    valid = []

    for correct, bug in BUG_PATTERNS:
        if correct in code:
            valid.append((correct, bug))

    if not valid:
        return None, None

    correct, bug = random.choice(valid)

    buggy_code = code.replace(correct, bug, 1)

    return buggy_code, correct
