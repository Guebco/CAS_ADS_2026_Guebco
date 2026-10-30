import re
import pytest

def add(x, y):
    """This function adds two numbers."""
    return x + y

def test_add():
    assert add(2, 3) == 5

def multiply(x, y):
    """This function multiplies two numbers."""
    return x * y

def test_multiply():
    assert multiply(2, 3) == 6

def find_longest_word(sentence):
    """
    Finds the longest word in a given sentence.

    This function ignores punctuation and considers words to be sequences of
    alphabetic characters. If the input is not a string, empty, or contains no
    alphabetic words, it returns None. In case of a tie (multiple words
    of the same maximum length), it returns the first one encountered.

    Args:
        sentence (str): The input string to search within.

    Returns:
        str or None: The longest word found, or None if no valid word is found.
    """
    if not isinstance(sentence, str) or not sentence:
        return None

    # Remove punctuation and split the sentence into words
    words = re.findall(r'[a-zA-Z]+', sentence)

    if not words:
        return None

    # Find the longest word
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

def test_find_longest_word():
    assert find_longest_word("A short sentence.") == "sentence"
    assert find_longest_word("") is None
    assert find_longest_word(12345) is None

numbers = [1, 2, 3, 4, 6, 8, 15]

def calc_mean(numbers):
    """
    Calculates the mean (average) of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float or None: The mean of the numbers, or None if the input is not a list
                       or is empty.
    """
    if not isinstance(numbers, list) or not numbers:
        return None

    return sum(numbers) / len(numbers)

print(calc_mean(numbers))

def test_calc_mean():
    assert calc_mean([1, 2, 3, 4, 5]) == 3.0
    assert calc_mean([]) is None
    assert calc_mean("not a list") is None