def _is_match(string):
    buffer = []
    open_brackets = {'(', '{', '['}
    closed_brackets = {')', '}', ']'}

    if string == '':
        return True

    for ch in string:
        if ch in open_brackets:
            buffer.append(ch)
        else:
            if ch in closed_brackets and len(buffer) == 0:
                return False

            if ch == ')' and buffer[-1] == '(':
                buffer.pop()
            elif ch == ')' and buffer[-1] != '(':
                return False

            if ch == '}' and buffer[-1] == '{':
                buffer.pop()
            elif ch == '}' and buffer[-1] != '{':
                return False

            if ch == ']' and buffer[-1] == '[':
                buffer.pop()
            elif ch == ']' and buffer[-1] != '[':
                return False

    if buffer:
        return False
    else:
        return True

def braces(values):
    ans = []

    for string in values:
        if _is_match(string):
            ans.append("YES")
        else:
            ans.append("NO")

    return ans

arr = ['{)', '{{(())}}', '[}']
print(braces(arr))

