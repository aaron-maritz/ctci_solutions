# Aaron Maritz, Question 4

# Given a string, write a function to check if it is a permutation of a palindrome
# Thoughts -> palindrome is same forwards and backwards
# Only real thing to check -> if the count of a letter is even -> good
# There can only be one character with an odd count, if 2 -> wont be allowed

def isPalPerm(str) :
    oddCount = 0
    counts = {}
    str = str.lower()
    for char in str :
        counts[char] = counts.get(char, 0) + 1
    for char in counts :
        if char != ' ' :
            if counts[char] % 2 == 1 :
                oddCount += 1
    return oddCount <= 1

if __name__ == '__main__' :
    print("Testing isPalindromePermutation")
    print(isPalPerm("Tact Coa"))
    print(isPalPerm("ab    c"))
    print(isPalPerm("a   a"))
    print(isPalPerm(""))
    print(isPalPerm("b"))
    print(isPalPerm("bbaa"))
    print(isPalPerm("b   a   b  z"))
