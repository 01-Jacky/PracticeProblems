from collections import defaultdict

# Complete the function below.

def _get_best_digit(points_dict):
    best_digit = -1
    max_score = float('-inf')
    for k, v in points_dict.items():
        if k - 1 not in points_dict and k + 1 not in points_dict:
            score = v
        elif k - 1 not in points_dict:
            score = v - points_dict[k + 1]
        elif k + 1 not in points_dict:
            score = v - points_dict[k - 1]
        else:
            score = v - points_dict[k + 1] - points_dict[k - 1]

        print('digit:{} score:{}'.format(k,score))
        if score > max_score:
            best_digit = k
            max_score = score
    return best_digit, points_dict[best_digit]


def maxPoints(elements):
    points_dict = defaultdict(int)

    for el in elements:
        points_dict[el] += el
    print(points_dict)

    total_score = 0
    while points_dict:
        k, score = _get_best_digit(points_dict)
        total_score += score

        if k - 1 not in points_dict and k + 1 not in points_dict:
            points_dict.pop(k)
        elif k - 1 not in points_dict:
            points_dict.pop(k)
            points_dict.pop(k + 1)
        elif k + 1 not in points_dict:
            points_dict.pop(k)
            points_dict.pop(k - 1)
        else:
            points_dict.pop(k)
            points_dict.pop(k + 1)
            points_dict.pop(k - 1)
    return total_score



print(maxPoints([3,3,4,2]))

