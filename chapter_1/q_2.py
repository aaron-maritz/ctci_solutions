# Aaron Maritz, Question 2
# Given two strings, write a method to determine if one is a permutation of the other

# Thoughts -> Sort both strings, return the comparison -> O(nlogn) time
# Second thought -> Put all chars of string 2 in a map
# For each char in string 1 -> check if it is in the map (decrement the value)
# Remember to check their lengths at the start
# O(n) time, O(n) space


# Returns True if str1 is a permutation of str2
# Else returns False
def isPermutation(str1, str2) :
    if len(str1) != len(str2) :
        return False
    counts = {}
    for char in str2 :
        counts[char] = counts.get(char, 0) + 1
    for char in str1 :
        if counts.get(char, 0) <= 0 :
            return False
        else :
            counts[char] = counts[char] - 1
    return True

def isPermutationTwo(str1, str2) :
    str1 = "".join(sorted(str1))
    str2 = "".join(sorted(str2))
    if str1 == str2 :
        return True
    return False

# Just change the function to isPermutationTwo to test that one
if __name__ == '__main__' :
    print("TestingIsPermutation: ")
    print("Testing a, a: %s", isPermutation("a", "a"))
    print("Testing ab, ba: %s", isPermutation("ab", "ba"))
    print("Testing aab, "": %s", isPermutation("aab", ""))
    print("Testing "", "": %s", isPermutation("", ""))
    print("Testing Aa, a: %s", isPermutation("Aa", "a"))
    print("Testing ABC, CBA: %s", isPermutation("ABC", "CBA"))
    print("Testing AbcDAC, abds: %s", isPermutation("AbcDAC", "abds"))
