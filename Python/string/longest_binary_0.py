def solution(N):
    s = "{0:b}".format(N)
    cur_count = 0
    longest_count = 0

    for c in s:
        if c == '0':
            cur_count += 1
        if c == '1':
            if cur_count > longest_count:
                longest_count = cur_count
            cur_count = 0
    return(longest_count)

print(solution(529))