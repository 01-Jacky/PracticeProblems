def _roman_to_int(s):
    table = {}
    table['I'] = 1
    table['V'] = 5
    table['X'] = 10
    table['L'] = 50

    if len(s) == 1:
        return table[s[0]]
    else:
        total = 0

        for i in range((len(s))):
            first = table[s[i]]
            if i+1 < len(s):
                second = table[s[i+1]]
            else:
                second = 0

            if first < second:
                total = total - first
            else:
                total = total + first

        return total

def getSortedList(names):
    ranking = {}

    for name in names:
        first_name = name.split(' ')[0]
        roman_numeral = name.split(' ')[1]
        roman_ordinal = _roman_to_int(roman_numeral)

        if first_name in ranking:
            ranking[first_name].append((roman_ordinal,roman_numeral))
        else:
            ranking[first_name] = [(roman_ordinal,roman_numeral)]

    ans = []
    for first_name in sorted(ranking):
        for ordinal in sorted(ranking[first_name]):
            ans.append((first_name + ' ' + ordinal[1]))

    return ans

arr = ['Philip IX','Philip II', 'Philippe VI']
print(getSortedList(arr))