"""
(2, 3)  # meeting from 10:00 – 10:30 am
(6, 9)  # meeting from 12:00 – 1:30 pm
Write a function merge_ranges() that takes a list of meeting time ranges and returns a list of condensed ranges.

Given:      [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
Return:     [(0, 1), (3, 8), (9, 12)]

Solution:
1) Brute force: for each pair, compare to all other pairs
Time O(N^2) Space O(N)

2) Sort by start time and then merge iteratively if needed
Time O(n log n) Space O(N)
"""

def merge_ranges(meetings):
    # Sort meetings
    meetings_sorted = sorted(meetings, key=lambda meeting: meeting[0])
    merged = [meetings_sorted[0]]

    # See if the next meeting needs to be merged with previous one
    for cur_meeting in meetings_sorted[1:]:
        prev_merged_start = merged[-1][0]
        prev_merged_end   = merged[-1][1]
        cur_meeting_start = cur_meeting[0]
        cur_meeting_end   = cur_meeting[1]

        if cur_meeting_start <= prev_merged_end:
            # Overlap fonud, take the later end time
            merged[-1] = (prev_merged_start, max(prev_merged_end, cur_meeting_end))
        else:
            # Else treat it as separate meeting
            merged.append(cur_meeting)

    return merged




print(merge_ranges([(0, 1),(4, 8), (3, 5), (10, 12), (9, 10)]))
# expects [(0, 1), (3, 8), (9, 12)]