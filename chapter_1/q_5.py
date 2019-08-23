#   Aaron Maritz
#   Question 1.5
#   One Away -> Three types of edits that can be performed on strings
#   Insert char, Remove char, Replace char, Given two strings determine if they are one edit (or zero) away
#   example -> pale, pale -> true,  ple, pale -> true,  pale, bake -> false

#   Thoughts  -> first check length, if length is >= 2 away -> false
#   Key is finding difference <= 1 between the two
#   Best run time -> O(n) where n is the length of the first string
#   Look at the seperate conditions



def oneAway(str1, str2) :
    if str1 == str2 :
        return True
    # At this point we know they are not the same string
    # Check if count(# of inconsistenceies is > 1)
    # If so -> return False
    ptr1 = 0
    ptr2 = 0
    count = 0
    len1 = len(str1)
    len2 = len(str2)
    if (abs(len1 - len2) >= 2) :
        return False
    # How to check if there was an inserted
    # Inserted check -> ptr2 -=
    # Remove check -> ptr1 -=
    # Edit check -> index stays the same
    while (ptr1 < len1):
        if ptr1 >= len2 or str1[ptr1] != str2[ptr2] : # inconsistency found
            count += 1
            if count > 1 :
                return False
            if len1 > len2 : # checking for insert
                ptr2 -= 1
            if len2 > len1 : # checking for remove
                ptr1 -= 1
        ptr2 += 1
        ptr1 += 1

    return True



if __name__ == '__main__' :
    print (oneAway(['p','l','e'], ['p','a','l','e']))
    print (oneAway(['p','a','l','e','s'], ['p','a','l','e']))
    print (oneAway(['p','a','l','e'], ['b','a','l','e']))
    print (oneAway(['p','a','l','e'], ['b','a','k','e']))
    print (oneAway([''], ['']))
    print (oneAway(['h','e'], []))
    print (oneAway(['h','e'], ['h']))
    print (oneAway(['h','e'], ['b']))
    print (oneAway(['b'], ['h','e']))
