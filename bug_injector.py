import random

BUG_PATTERNS = [

# LOOP BOUNDARY ERRORS
("i<n", "i<=n"),
("i<n", "i<n-1"),
("i<=n", "i<n"),
("i>=0", "i>0"),
("i>0", "i>=0"),

# COMPARISON ERRORS
("==", "="),
(">", "<"),
("<", ">"),
(">=", "<="),
("<=", ">="),

# ARRAY INDEX ERRORS
("arr[i]", "arr[n]"),
("arr[i]", "arr[i+1]"),
("arr[i]", "arr[i-1]"),

# VARIABLE MISUSE
("sum", "count"),
("count", "sum"),
("max", "min"),
("min", "max"),

# INITIALIZATION ERRORS
("sum=0", "sum=1"),
("count=0", "count=1"),
("product=1", "product=0"),
("flag=1", "flag=0"),

# ARITHMETIC ERRORS
("+=", "-="),
("+=", "*="),
("*=", "+="),
("-=", "+="),

# CONDITION ERRORS
("%2==0", "%2=0"),
("%2==0", "%2!=0"),
("n%i==0", "n%i=0"),

# INCREMENT / DECREMENT ERRORS
("i++", "i--"),
("i--", "i++"),
("count++", "count--"),
("count--", "count++"),

# LOOP UPDATE ERRORS
("i++", ""),
("count++", ""),

# WRONG CONSTANTS
("10", "9"),
("10", "11"),
("1", "0"),
("0", "1"),

# MATRIX INDEX ERRORS
("mat[i][j]", "mat[j][i]"),
("mat[i][i]", "mat[i][j]"),

# STRING INDEX ERRORS
("str[i]", "str[len]"),
("str[i]", "str[i+1]"),

# SEARCH LOGIC ERRORS
("pos=i", "pos=-1"),
("found=1", "found=0"),

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
