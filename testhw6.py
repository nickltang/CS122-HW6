# ---------------------------------
# Name: testhw6
# Purpose: To test homework6 module
#
# Author: Nick Tang, Yuto Yoshimori
# ---------------------------------

import unittest
import homework6


class TestHomework6FinalGrade(unittest.TestCase):
    """
    Test case for execution of final_grade method
    """

    def setUp(self):
        """ Create dictionaries for testing """
        self.empty_dict = {}
        self.nonempty_dict = {'Nick': 88, 'Bob': 92, 'Joe': 74, 'Jane': 82,
                              'Emily': 52}

    def test_final_grade_default(self):
        """
        Test final_grade with default function (no extra credit argument)
        """
        self.assertEqual(homework6.final_grade(self.nonempty_dict),
                         {'Nick': 89, 'Bob': 93, 'Joe': 75, 'Jane': 83,
                          'Emily': 53})

    def test_final_grade_empty(self):
        """
        Test final_grade with empty dictionary argument
        """
        self.assertEqual(homework6.final_grade(self.empty_dict, 3), {})
        self.assertEqual(self.empty_dict, {})

    def test_final_grade_nonempty(self):
        """
        Test final_grade with nonempty dictionary argument
        """
        self.assertEqual(homework6.final_grade(self.empty_dict, 3), {})
        self.assertEqual(self.nonempty_dict, {'Nick': 88, 'Bob': 92,
                                              'Joe': 74, 'Jane': 82,
                                              'Emily': 52})


class TestHomework6MostWords(unittest.TestCase):
    """
    Test case for execution of most_words method
    """

    def setUp(self):
        """
        Create arguments lists for testing
        """
        self.one_arg = "Python"
        self.many_args = "python", "Python", "JavaScript", "java", \
            "haskell", "Typescript"

    def test_most_words_noargs(self):
        """
        Test most_words with no arguments
        """
        self.assertEqual(homework6.most_words(), None)

    def test_most_words_onearg(self):
        """
        Test most_words with one argument
        """
        self.assertEqual(homework6.most_words(self.one_arg), "Python")
        self.assertEqual(self.one_arg, "Python")

    def test_most_words_manyargs(self):
        """ Test most_words with many arguments """
        self.assertEqual(homework6.most_words(*self.many_args), "JavaScript")
        self.assertEqual(self.many_args, ("python", "Python", "JavaScript",
                                          "java", "haskell", "Typescript"))


if __name__ == '__main__':
    unittest.main()
