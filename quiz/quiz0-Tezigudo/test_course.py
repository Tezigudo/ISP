"""
Tests of the Course class.
These tests require pytest be installed.
Run these tests using 'pytest -v test_course.py' 
(-v is optional)
"""

from course import Course
import pytest


# some test courses
isp =   Course('01219245', 'Individual Software Process', 4)
prog2 = Course('01219116', 'Programming 2', 3)
algo1 = Course('01219217', 'Algo & Data Structures 1', 3)
algo2 = Course('01219218', 'Algo & Data Structures 2', 3)


def test_constructor():
    """Constructor should allow valid arguments."""
    prog1 = Course('204111', "P1", 1)
    # zero credits is allowed
    non_credit_course = Course('01201111', "Man and Society", 0)
    # cannot create a course with id or description that is empty or whitespace
    for invalid_arg in ['', ' ', '        ']:
        with pytest.raises(ValueError):
            bad_course = Course(invalid_arg, "Anonymous", 3)
        with pytest.raises(ValueError):
            bad_course = Course('01219111', invalid_arg, 2)
    # credits must be an integer
    with pytest.raises(TypeError):
        bad_course = Course('01219245', "Programming 0", "3")
        

def test_course_id():
    """course_id is a read-only property."""
    assert isp.course_id == '01219245'
    assert prog2.course_id == '01219116'
    with pytest.raises(AttributeError):
        isp.course_id = '01234567'

def test_course_id():
    """course_id is a read-only property."""
    assert isp.course_id == '01219245'
    assert prog2.course_id == '01219116'
    with pytest.raises(AttributeError):
        isp.course_id = '01234567'


def test_description():
    """course description is a read-only property."""
    assert isp.description == 'Individual Software Process'
    assert prog2.description == 'Programming 2'
    with pytest.raises(AttributeError):
        isp.description = 'ISP, of course'


def test_credits():
    """course credits is a read-only property."""
    assert isp.credits == 4
    assert prog2.credits == 3
    with pytest.raises(AttributeError):
        isp.credits = 2


def test_equals():
    """Equals should use the standard template."""
    assert isp.__eq__(isp)
    assert isp.__eq__(prog2) is False
    isp2 = Course("01219245", "Individual Software Process", 4)
    assert isp.__eq__(isp2)
    isp3 = Course("01219246", "Individual Software Process", 4)
    assert isp.__eq__(isp3) is False
    isp4 = Course("01219245", "Individual Software Processes", 4)
    assert isp.__eq__(isp4) is False
    isp5 = Course("01219245", "Individual Software Process", 1)
    assert isp.__eq__(isp5) is False


def test_equal_must_be_course():
    """Equals can only compare course objects. If arg not a course it should return false."""
    assert isp.__eq__(0) is False
    assert isp.__eq__("01219245 Individual Software Process (3)") is False


def test_str():
    """String value is correctly formatted."""
    assert str(isp) == "01219245 Individual Software Process (4)"
    assert str(prog2) == "01219116 Programming 2 (3)"
    non_credit = Course("01219000", "No Credit", 0)
    assert str(non_credit) == "01219000 No Credit (0)"
    big_course = Course("01234567890", "No Limit on Length of Course Descripton", 9999)
    assert str(big_course) == "01234567890 No Limit on Length of Course Descripton (9999)"


def test_can_sort():
    """Problem 4: Can sort a list of courses if Course is comparable."""
    courses = [isp, algo1, prog2]
    courses.sort()
    assert courses[0] == prog2
    assert courses[1] == algo1
    assert courses[2] == isp