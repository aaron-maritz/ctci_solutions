# Aaron Maritz, Question 1.6
# Implement a method to perform basic string compression using
# the counts of repeated characters
# aabcccccaaa -> a2b1c5a3
# assume string has only uppercase and lowercase letters

# thoughts -> string builder?
# Loop through the string ->
# compressd string len -> 2x number of unique characters

# Equivalent to string builder for python is add to a list
# Then join at the end

def compress(input) :
    # Sanity check here
    if len(input) <= 1 :
        return input
    str1 = list(input)
    index = 0
    str2 = []
    for char in range (1, len(str1)) :
        if str1[char] != str1[char - 1] :
            str2.append(str1[char - 1])
            str2.append(str(char - index))
            index = char
    # Gotta get the last fencepost
    str2.append(str1[len(str1) - 1])
    str2.append(str(char - index + 1))
    if len(str1) <= len(str2) :
        return input
    return ''.join(str2)

if __name__ == '__main__' :
    print(compress('aabcccccaaa'))
    print(compress(''))
    print(compress('a'))
    print(compress('ab'))
    print(compress('abca'))
    print(compress('abbbbbbbbbBc'))
