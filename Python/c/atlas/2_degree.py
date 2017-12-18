from collections import defaultdict

def _build_index_map(arr):
    """ Builds an index map of digits and returns a tuple of the map and the max degree"""
    # index_map[1]->[1,5] means digit 1 appear in index 1 and 5
    # len_map helps get max degree as we're building index_map (better than iterating through index_map in the end)
    max_degree = 0
    index_map = defaultdict(list)
    len_map = defaultdict(int)

    for i, el in enumerate(arr):
        index_map[el].append(i)
        len_map[el] += 1
        if len_map[el] > max_degree:
            max_degree = len_map[el]

    return max_degree, index_map

def min_size_degree(arr):
    # Build a map of index such that index_map[1]->[1,5] means digit 1 appears in indexes: 1,5
    max_degree, index_map = _build_index_map(arr)
    shortest_subarr = len(arr)

    # Calculate the arr length for each digit that meets the max degree; track the shortest length
    for index_arr in index_map.values():
        if len(index_arr) == max_degree:
            subarr_length = index_arr[-1] - index_arr[0] + 1    # len of subarr = last index - first + 1
            if subarr_length < shortest_subarr:
                shortest_subarr = subarr_length
    return shortest_subarr

print(min_size_degree([1,2,2,3,1]))
print(min_size_degree([1,1,2,1,2,2]))
# print(min_size_degree([1,2,2,3,1,4,1]))
print(min_size_degree([1,2,1,1,2,2,2]))

