import unittest
from string_manipulation import (count_vowels, reverse_string, is_palindrome,
                                 remove_duplicates, capitalize_words,
                                 replace_substring, find_longest_word,
                                 word_frequency, anagram_check, extract_digits,
                                 find_most_frequent_char, remove_special_characters)

class TestStringManipulation(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("AEIOU"), 5)

    def test_reverse_string(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("12345"), "54321")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates("programming"), "progamin")
        self.assertEqual(remove_duplicates("aaaaaa"), "a")
        self.assertEqual(remove_duplicates("abcd"), "abcd")

    def test_capitalize_words(self):
        self.assertEqual(capitalize_words("hello world from python"), "Hello World From Python")
        self.assertEqual(capitalize_words(""), "")
        self.assertEqual(capitalize_words("PYTHON"), "Python")

    def test_replace_substring(self):
        self.assertEqual(replace_substring("the quick brown fox", "fox", "dog"), "the quick brown dog")
        self.assertEqual(replace_substring("hello world", "world", "there"), "hello there")
        self.assertEqual(replace_substring("repeat repeat", "repeat", "done"), "done done")

    def test_find_longest_word(self):
        self.assertEqual(find_longest_word("The quick brown fox jumped over the lazy dog"), "jumped")
        self.assertEqual(find_longest_word("short longest word"), "longest")
        self.assertEqual(find_longest_word("equal size test"), "equal")

    def test_word_frequency(self):
        self.assertEqual(word_frequency("apple banana apple orange banana apple"),
                         {'apple': 3, 'banana': 2, 'orange': 1})
        self.assertEqual(word_frequency("test test test"), {'test': 3})
        self.assertEqual(word_frequency("one word"), {'one': 1, 'word': 1})

    def test_anagram_check(self):
        self.assertTrue(anagram_check("Listen", "Silent"))
        self.assertFalse(anagram_check("Hello", "World"))
        self.assertTrue(anagram_check("Dormitory", "Dirty room"))

    def test_extract_digits(self):
        self.assertEqual(extract_digits("My phone number is 123-456-7890"), "1234567890")
        self.assertEqual(extract_digits("No digits here!"), "")
        self.assertEqual(extract_digits("Year 2024"), "2024")

    def test_find_most_frequent_char(self):
        self.assertEqual(find_most_frequent_char("sample string"), 's')
        self.assertEqual(find_most_frequent_char("banana"), 'a')
        self.assertEqual(find_most_frequent_char("abcdabcd"), 'a')  # Tie, returns first 'a'

    def test_remove_special_characters(self):
        self.assertEqual(remove_special_characters("Hello, World! @2024"), "Hello World 2024")
        self.assertEqual(remove_special_characters("Python#is$fun!"), "Pythonisfun")
        self.assertEqual(remove_special_characters("No special chars"), "No special chars")

if __name__ == '__main__':
    unittest.main()
