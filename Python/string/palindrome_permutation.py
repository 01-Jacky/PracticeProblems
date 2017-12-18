def is_paldinrome_permutation(s):
    odd_freq_char = set()
    for ch in s:
        if ch in odd_freq_char:
            odd_freq_char.remove(ch)
        else:
            odd_freq_char.add(ch)

    if len(odd_freq_char) < 2:
        return True
    else:
        return False