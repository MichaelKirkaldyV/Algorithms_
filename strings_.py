#Write a function to check whether two given strings are Permutation of each other or not. A Permutation of a string is another string that contains same characters, only the order of characters can be different. For example, “abcd” and “dabc” are Permutation of each other.

def checkPerm(str1, str2):
    # Check to see if the strings are equal, if not they aren't permutations. Permutations have equal characters!
    s1 = len(str1)
    s2 = len(str2)
    if s1 != s2:
        return False
    
    # Wwe should sort the strings and see if each character is equal to another. If so then we have permutations.
    a = sorted(str1)
    b = sorted(str2)
    print(a, b)

    # Check if the character of the sorted string are equal, if so then we have a permutation.
    for x in range(0, s1):
        if a[x] != b[x]:
            return False

    # If all test cases pass then it is a permutation.       
    return True


a = "abddd"
b = "adddb"
print(checkPerm(a, b))

def urlify(str):

    # Strips strings on all tailing and preceding spaces.
    str.strip(" ")

    # Replaces all other spaces with %20
    s = str.replace(" ", "%20")

    return s

str_ = "Hello motto "
print(urlify(str))

