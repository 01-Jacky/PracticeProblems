"""
'> >  <  < > > * >  <'
 1 1 -1 -1 1 1   1 -1    values
           2            multiplier

'> > > * > *  < * > >'
 1 1 1   1   -1   1 1    values
   2*2*2                 multiplier

1st generate value array by decoding >, < and ignoring *
[1 1 1 0 1 0 -1 0 1 1] value array

Seperately generate multiplier array by decoding *
[1 1 1 2 1 2 1 2 1 1] 1st pass to get places where that's a 2x multiplier
[1 1 1 8 1 1 1 1 1 1] 2nd pass to take care of stacked multiplier effect ( if we see a 2 look ahead to see if it stack)
[1 1 8 1 1 1 1 1 1 1] final post processing shift left 1 so it lines up with value array

Them the year difference is the sum product by element in each array
[1 1 1 0 1 0 -1 0 1 1]
[1 1 8 1 1 1 1 1 1 1]

1*1 + 1*1 + 1*8 + 0*1 + .... = year_change

return 2017 - year change

"""

def solve_year(input):
    CUR_YEAR = 2017
    values = input

    value_arr = []
    for el in values:
        if el == '>':
            value_arr.append(1)
        elif el == '<':
            value_arr.append(-1)
        else:
            value_arr.append(0)

    # 1st pass
    multiplier_arr = [1] * len(values)
    for i in range(len(values)):
        if values[i] == '*':
            multiplier_arr[i] = 2

    # 2nd pass
    for i in range(len(multiplier_arr)-1, -1, -1):
        if multiplier_arr[i] != 1 and multiplier_arr[i-2] != 1:
            new_value = multiplier_arr[i-2] * multiplier_arr[i]
            multiplier_arr[i-2] = new_value
            multiplier_arr[i] = 1

    multiplier_arr = multiplier_arr[2:] + [1,1]   # shift left one to make the 2 array line up

    print(value_arr)
    print(multiplier_arr)

    # merge the two
    year_change = 0
    for i in range(len(value_arr)):
        year_change += value_arr[i] * multiplier_arr[i]

    return CUR_YEAR + year_change


# msg1 = '> > < < > > * > <'
# print(solve_year(msg1))
#
msg2 = '>>>*>*<*>>'

# msg2 = '>>*>>'


# encrpyted_msg = input()
print(solve_year(msg2))

