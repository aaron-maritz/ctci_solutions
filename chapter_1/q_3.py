# Aaron Maritz, Question 3

# Write a method to replace all spaces in a string with %20
# Can assume there is enough length, and given the 'true length' as 2nd arg
# This is so we can cut off leading/trailing spaces

# Thoughts -> trim the beginning/end of string
# Then, take the string and turn it into a list -> join with "%20"
# Strip -> Atleast O(n) -> split O(n) space -> join ?

def URLify(str, length) :
    str = str.strip()
    lst = str.split(" ")
    str = "%20".join(lst)
    return str

def URLify2(str, length) :
    spaces = 0
    for char in range (length) :
        if str[char] == ' ' :
            spaces += 1
    total = spaces * 2 + length
    str[total] = '\0'
    total = total - 1
    for i in reversed(range(0, length)) :
        if str[i] == ' ' :
            str[total] = '0'
            str[total - 1] = '2'
            str[total - 2] = '%'
            total = total - 3
        else :
            str[total] = str[i]
            total = total - 1
    print (str)

if __name__ == '__main__' :
    print("Testing URLify")
    URLify2( ['a',' ','m','a','n',' ','d','o','e','s',' ',' ',' ',' ',' '], 10 )
    URLify2( ['n','o','n','e',' '], 4 )
    URLify2( [' '], 0 )
    URLify2( ['e','x','c','e','s','s',' ',' ','m','e',' ',' ',' ',' ',' '], 10 )


# Algorithm to do this in place -> given we had a character array
# [h, e, l, l, o, , i, t, s, , m, e, , , , , , ] -> 12 length
# Number of spaces -> iterate over range len -> counts where char = ' '
# Then end of the string is true length + 2x spaces = total length
# Put a \0 termination character at index total length and have an index pointer
# Iterate starting from index true length - 1 in array ->
# if char at i is not a space -> make the index pointer that char
# else make index pointer 0, then index -1 -> 2, then index - 2 -> %
# Going backwards makes it so you don't have to do any shifting
# update index -= 1, or -=3 depending on case, go till index from true length = 0.
