Let's say you have a list of N+1 integers between 1 and N. You know there's at least one duplicate, but there might be more. For example, if N=3, your list might be 3, 1, 1, 3 or it might be 1, 3, 2, 2. Print out a number that appears in the list more than once. (That is, in the first example, you can print '1' or '3' -- you don't have to print both.)

N=3
len = 4

3 1 1 3     1 or 3
1 3 2 2     2
1 1 1 1     1

1) Use a set
3 1 1 3

set 3 1

2) No extra memory, sort first
3 1 1 3
1 1 3 3

3) No ememory, cant modify inputs
2 1 1 3

2 x x x

<2     >=2
1 1    3
