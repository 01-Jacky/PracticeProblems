""" check balanced parenthesis string, """

def is_balanced(s):
    counter = 0
    for ch in s:
        if ch == '(':
            counter += 1
        elif ch == ')':
            counter -= 1

            if counter < 0:     # optimization: short circuit as soon as there isn't enough ( to match a )
                return False

    if counter == 0:
        return True
    else:
        return False

valid_string = 'x+(a*b*(c*d))-y'
invalid_string = '(x+(a*b*(c*d))-y)'
print(is_balanced(valid_string))
print(is_balanced(invalid_string))