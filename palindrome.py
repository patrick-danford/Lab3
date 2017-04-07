# String Palindrome

"""
Patrick Danford 
Lab 3, String Palindrome

A string is a palindrome if it remains unchanged when reversed, 
for example "dad" is a palindrome as reverse of "dad" is "dad" 
whereas "program" is not a palindrome.

"""


def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

print is_palindrome(raw_input("Enter a word: "))
