# Aaron Maritz, Question 1
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# First thoughts -> see every character -> put them in a hashmap -> check if counts >2 for any character
# -> O(n) time & space
# Now without data structures -> Sort them -> check if any character is equal to an adjacent character
# -> O(nlogn) time


def isUnique(str) :
    counts = {}
    for char in str :
        counts[char] = counts.get(char, 0) + 1 # returns 0 if not in dict, else the current value
    for char in counts :
        if counts[char] > 1 :
            return False
    return True

if __name__ == '__main__':
    print("Testing isUnique:")
    print("Testing a %s", isUnique("a"))
    print("Testing ab: %s", isUnique("ab"))
    print("Testing aab: %s", isUnique("aab"))
    print("Testing "": %s", isUnique(""))
    print("Testing Aa: %s", isUnique("Aa"))
    print("Testing ABC %s", isUnique("ABC"))
    print("Testing AbcDAC %s", isUnique("AbcDAC"))
