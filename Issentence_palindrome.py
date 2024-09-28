def is_palindrome(string:str) -> bool:
    return string[::-1].casefold() == string.casefold()

def is_palindrome2(sentence:str) -> bool:
    """
    States if a `string` is a palindrome
    :param sentence:The `string` that the user types in when prompted to enter the value
    The function is case-insensitive and ignores whitespace and capitalisation
    :return: Returns `True` if the sentence is a Palindrome, otherwise returns `False`
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
    print(f"{word} is a palindrome")
else:
    print(f"{word}is Not a palindrome")
