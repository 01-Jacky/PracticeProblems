def merge_lists(lst_a, lst_b):
    # set up our merged_list
    merged_list_size = len(lst_a) + len(lst_b)
    merged_list = [None] * merged_list_size

    index_b = 0
    index_a = 0
    index_merged = 0

    while index_merged < merged_list_size:
        lst_a_ended = index_a >= len(lst_a)
        lst_b_ended = index_b >= len(lst_b)

        # my list must not be exhausted, and EITHER:
        # 1) Alice's list IS exhausted, or
        # 2) the current element in my list is less
        #    than the current element in Alice's list
        if not lst_a_ended and (lst_b_ended or (lst_a[index_a] < lst_b[index_b])):
            merged_list[index_merged] = lst_a[index_a]
            index_a += 1
        else:    # work on list b
            merged_list[index_merged] = lst_b[index_b]
            index_b += 1

        index_merged += 1
    return merged_list


def merge_lists_mine(lst_a, lst_b):
    # set up our merged_list
    merged_list = [None] * (len(lst_a) + len(lst_b))

    index_b = 0
    index_a = 0
    index_merged = 0

    while index_a < len(lst_a) or index_b < len(lst_b):         # while either list has elements
        # if a has elements and (b is empty or b has a smaller element)
        if index_a < len(lst_a) and index_a < len(lst_b):       # if both list has elements
            if lst_a[index_a] < lst_b[index_b]:
                merged_list[index_merged] = lst_a[index_a]
                index_a += 1
            else:
                merged_list[index_merged] = lst_b[index_b]
                index_b += 1
        elif index_a < len(lst_a):                              # if a has element and b empty
            merged_list[index_merged] = lst_a[index_a]
            index_a += 1
        else:                                                   # if b has elements and a empty
            merged_list[index_merged] = lst_b[index_b]
            index_b += 1
        index_merged += 1

    return merged_list


my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19, 20, 23]
print(merge_lists(my_list, alices_list))
print(merge_lists_mine(my_list, alices_list))
