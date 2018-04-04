def _is_match(string):
    if string == '':
        return 'YES'

    for ch in string:
        if ch in open_brackets:
            buffer.append(ch)
        else:
            if ch in closed_brackets and len(buffer) == 0:
                ans.append('NO')
                test = False
                break

            if ch == ')' and buffer[-1] == '(':
                buffer.pop()
            elif ch == ')' and buffer[-1] != '(':
                ans.append('NO')
                test = False
                break

            if ch == '}' and buffer[-1] == '{':
                buffer.pop()
            elif ch == '}' and buffer[-1] != '{':
                ans.append('NO')
                test = False
                break

            if ch == ']' and buffer[-1] == '[':
                buffer.pop()
            elif ch == ']' and buffer[-1] != '[':
                ans.append('NO')
                test = False
                break

    if test:
        if buffer:
            ans.append('NO')
        else:
            ans.append('YES')

def braces(values):
    buffer = []
    open_brackets = {'(', '{', '['}
    closed_brackets = {')', '}', ']'}

    ans = []

    for string in values:
        print(string)


    return ans

arr = ['','{[}]', '{{(())}}']
print(braces(arr))

