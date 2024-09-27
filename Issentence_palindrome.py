def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


def is_palindrome2(sentence):
    """
    States if a string is a palindrome
    :param sentence:The string that the user types in when prompted to enter the value
    :return: Returns a boolean vale
    """
    string=""
    for char in sentence:
        if char.isalnum():
            string+=char
        return is_palindrome(string)
        # sentence=''.join([char for char in sentence if char.isalpha()])
        # return sentence[::-1].casefold() == sentence.casefold()

word=input("Write a sentence")
if is_palindrome2(word):
    print("That sentence is a palindrome")
else:
    print("That sentence is NOT a palindrome")
