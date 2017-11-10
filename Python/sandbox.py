def perm(s):
    if len(s) <= 1:
        return s

    ans = [[s[0]]]
    print(ans)

    for i in range(1, len(s)):
        print('inserting i = {}'.format(i))

        tmp = []
        for e in ans:
            get_inserted_values(e, s[i], i)
            temp.append()
        tmp.append(0)

        # for j in range(i+1):
        #     ans.append(ans[0])
        # print(ans)

    print(ans)

s = '123'
perm([c for c in s])