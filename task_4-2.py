from re import T
import re
from tkinter.messagebox import RETRY


def is_palindrome(text: str):
    """
    Function checking if text is a palindrome.
    Return True if text is palindrome 
    and False if text is not palindrome
    """
    for i in range(len(text) // 2):
        if (text[i] != text[-(i + 1)]):
            return False
    return True

result = is_palindrome("kajak")
print(f"Is word kajak a palindrome? {result}")
result = is_palindrome("text")
print(f"Is word text a palindrome? {result}")
