"""
1)
Map string to pattern string
cat -> a
dog -> b
doggy ->

used:
a
b
For each string check the mapping

Watch out for cat dog dog, a b c
and
cat dog
"""

def areFollowingPatterns(strings, patterns):
    mapping = {}
    seen = set()

    for i in range(len(strings)):
        s = strings[i]
        ch = patterns[i]

        if s not in mapping:
            if ch in seen:          # Take care of cases like: cat dog doggy | a b b
                return False
            else:
                mapping[s] = ch
                seen.add(ch)
        else:
            if mapping[s] != ch:
                return False

    return True


