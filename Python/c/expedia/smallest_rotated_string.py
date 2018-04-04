"""
Write code to find lexicographic minimum in a circular array, e.g. for the array BCABDADAB, the lexicographic minimum is ABBCABDAD

1)Generate all rotations, then sort them to get the top 1
To get all rotation we can write a function that takes the first ch and append it to the end
or we can use this trick
ABBCABDAD
ABBCABDADABBCABDAD
^       ^
 ^       ^
  ^       ^
Time O(N^2) Space O(N)
"""

def lex_min(str):
    n = len(str)
    arr = []
    warped_str = str + str      # used to quickly find rotation

    for i in range(n):                  # n
        arr.append(warped_str[i:i+n])       #n

    arr.sort()
    return arr[0]


print(lex_min('BCABDADAB'))

"""
string minLexRotation(string str)
{
    // Find length of given string
    int n = str.length();
 
    // Create an array of strings to store all rotations
    string arr[n];
 
    // Create a concatenation of string with itself
    string concat = str + str;
 
    // One by one store all rotations of str in array.
    // A rotation is obtained by getting a substring of concat
    for (int i = 0; i < n; i++)
        arr[i] = concat.substr(i, n);
 
    // Sort all rotations
    sort(arr, arr+n);
 
    // Return the first rotation from the sorted array
    return arr[0];
}"""