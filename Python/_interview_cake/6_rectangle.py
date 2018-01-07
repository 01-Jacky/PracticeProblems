"""
  my_rectangle = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 1,

    # width and height
    'width': 6,
    'height': 3,

}

Solution:
1) If both x overlap and y overlap, then we have intersection
"""

def find_range_overlap_v2(point1, length1, point2, length2):
    pass


def find_range_overlap(point1, length1, point2, length2):
    # find the highest start point and lowest end point.
    # the highest ("rightmost" or "upmost") start point is the start point of the overlap.
    # the lowest end point is the end point of the overlap.
    highest_start_point = max(point1, point2)
    lowest_end_point = min(point1 + length1, point2 + length2)

    # return null overlap if there is no overlap, else return the overlap length
    if highest_start_point >= lowest_end_point:
        return (None, None)
    else:
        overlap_length = lowest_end_point - highest_start_point
        return (highest_start_point, overlap_length)


def find_rectangular_overlap(rect1, rect2):
    # get the x and y overlap points and lengths
    x_overlap_point, overlap_width  = find_range_overlap(
        rect1['left_x'], rect1['width'],  rect2['left_x'], rect2['width'])
    y_overlap_point, overlap_height = find_range_overlap(
        rect1['bottom_y'], rect1['height'], rect2['bottom_y'], rect2['height'])

    # return null rectangle if there is no overlap
    if not overlap_width or not overlap_height:
        return {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
    else:
        return {
            'left_x': x_overlap_point,
            'bottom_y': y_overlap_point,
            'width': overlap_width,
            'height': overlap_height,
        }

point1, length1, point2, length2 = 0, 5, 3, 7
print(find_range_overlap(point1, length1, point2, length2))
print(find_range_overlap_v2(point1, length1, point2, length2))