palin = "madame"


def is_alpha_num(string):
    return True if string.isalnum() else False
def to_lower_case(string):
    return string.lower()
def is_valid_palindrome(test_string):
    test_string = list(filter(is_alpha_num,test_string))
    test_string = list(map(to_lower_case,test_string))
    print(test_string)
    for i in range(len(test_string)//2):
        if test_string[i] == test_string[len(test_string)-1-i]:
            pass
        else :
            return False
    return True

print(is_valid_palindrome("A man, a plan, a canal: Panama"
))

