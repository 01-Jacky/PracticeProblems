def valid(expression):
    openbrackets = set(['{', '(', '['])
    closed = set(['}', ')', ']'])
    pair = {
        ')':'(',
        ']':'[',
        '}':'{'
    }

    stack = []
    for c in expression:
        if c in openbrackets:
            stack.append(c)

        if c in closed:
            if len(stack) == 0:
                return False
            elif stack[-1] == pair[c]:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

assert valid('{[()]}') == True
assert valid('{[(])}') == False
assert valid('{{[[(())]]}}') == True

