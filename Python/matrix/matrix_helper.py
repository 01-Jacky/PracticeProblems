def print_matrix(matrix):
    for row in matrix:
        lst = [str(el).rjust(2,' ') for el in row]
        # print(lst)
        print(" ".join(lst))

    print()

if __name__ == '__main__':
    print_matrix([
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]
            ])