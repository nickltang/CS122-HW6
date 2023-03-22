# ---------------------------------
# Name: homework6
# Purpose: Base file with functions so we can demonstrate unittest
# library in testhw6
#
# Author: Nick Tang, Yuto Yoshimori
# ---------------------------------


def final_grade(student_grades, ec_points=1):
    """
    Adds extra credit points to students' grades within student_grades
    dictionary.

    :param student_grades: (dict) student names mapped to their grades
    :param ec_points: (int) number of extra credit points to add
                        if no ec_points
    :return: (dict)
    """
    return {student: student_grades[student] + 1 for student in
            student_grades}


def most_words(*args):
    """

    :param args: (str) sequence of 0 or more strings
    :return: (str) if args is empty return None
        Else, return the longest string in args
    """
    if not args:
        return None
    longest_str = lambda word_list: max(word_list, key=len)
    return longest_str(args)