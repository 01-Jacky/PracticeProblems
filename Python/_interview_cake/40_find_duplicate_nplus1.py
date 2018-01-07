def find_repeat(lst):
    floor = 1
    ceiling = len(lst) - 1

    while floor < ceiling:
        # divide our range 1..n into an upper range and lower range (such that they don't overlap)
        # lower range is floor..midpoint, upper range is midpoint+1..ceiling
        midpoint            = floor + ((ceiling - floor) // 2)
        lower_range_floor   = floor
        lower_range_ceiling = midpoint
        upper_range_floor   = midpoint + 1
        upper_range_ceiling = ceiling
        distinct_ints_in_lower_range = lower_range_ceiling - lower_range_floor + 1

        # count number of items in lower range. Is it in the lower range?
        items_in_lower_range = 0
        for item in lst:
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        # there must be a duplicate in lower range or upper, so update the range and repeat until no more
        if items_in_lower_range > distinct_ints_in_lower_range:
            floor = lower_range_floor
            ceiling = lower_range_ceiling
        else:
            floor = upper_range_floor
            ceiling =  upper_range_ceiling

    # floor and ceiling have converged we found a number that repeats!
    return floor

def find_repeat_mutates_my_list(lst):
    lst.sort()

    for i in range(len(lst)-2):
        if lst[i] == lst[i+1]:
            return lst[i]
    return -1



# print(find_repeat([1,2,3,4,5,4]))
print(find_repeat_mutates_my_list([1,2,3,4,5,4]))