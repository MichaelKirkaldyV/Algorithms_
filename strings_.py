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

# For a given sentence, return the average word length. 
# Note: Remember to remove punctuation first.

def avgWordLength(str):
    # This sets every index without a punctuation to a space.
    for i in "!?,.''$":
        str = str.replace(i, " ")

    # Splits string into a list.
    str_list = str.split()

    # Generator. Round and return the sum of the length of every word for each word in string list, divided 2.
    return round(sum(len(word) for word in str_list/len(str_list), 2)



str_2 = "When are we going to Japan?"
str_3 = "Hi my name is Imir, May I ask what is yours?"
print(avgWordLength(str_2))
print(avgWordLength(str_3))

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Notes:
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.
def AddStrings(num1, num2):
    
    #eval() adds all the numbers in the int together, then we can add them return them using str() which makes them a string.
    return str(eval(num1) + eval(num2))


num_1 = '678'
num_2 = '1209'
print(addString(num_1, num_2))