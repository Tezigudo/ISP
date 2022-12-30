"""
Tests of CourseList using pytest.
In ISP we will mostly use unittest.  I use pytest here
because it's easier to read and trace the failure messages.

Run these tests using 'pytest -v test_courselist.py' 
(-v is optional) or simply run this file with python3.
"""

from course import Course
from courselist import CourseList

# some test courses
isp =   Course('01219245', 'Individual Software Process', 4) # more credits!
prog2 = Course('01219116', 'Programming 2', 3)
algo1 = Course('01219217', 'Algo & Data Structures 1', 3)
algo2 = Course('01219218', 'Algo & Data Structures 2', 3)


def test_add_courses():
    """Can add courses to the CourseList and get them later."""
    courselist = CourseList()
    assert courselist.add_course(isp)
    assert courselist.add_course(prog2)
    # cannot add the same course again
    assert not courselist.add_course(isp)
    assert not courselist.add_course(prog2)
    # we can get a course from CourseList using its course_id
    assert courselist.get_course('01219245') is isp
    assert courselist.get_course('01219116') is prog2
    # we get None for a course not in our courselist
    course = courselist.get_course('01219499')
    assert course is None


def test_drop_course():
    """Can drop a course after enrolling."""
    courselist = CourseList()
    assert courselist.add_course(isp)
    assert courselist.add_course(prog2)
    assert courselist.add_course(algo1)
    # ISP is too much work. Drop it!
    assert courselist.drop_course('01219245')
    # should not be enrolled now
    assert courselist.get_course('01219245') is None
    # cannot drop again (returns False)
    assert courselist.drop_course('01219245') is False
    # We are still be enrolled in Algorithms 1
    assert courselist.get_course('01219217') is algo1
    # Drop Algorithms 1
    assert courselist.drop_course('01219217')
    # Not enrolled now
    assert courselist.get_course('01219217') is None


def test_get_credits():
    """Courselist computes the number of credits we are enrolled in."""
    courselist = CourseList()
    assert courselist.get_credits() == 0
    total_credits = 0
    for course in [isp, prog2, algo1]:
        total_credits += course.credits
        courselist.add_course(course)
        assert courselist.get_credits() == total_credits
    # after dropping a course, the credits are reduced
    courselist.drop_course('01219217')
    total_credits -= algo1.credits
    assert courselist.get_credits() == total_credits
    # dropping junk has no effect
    try:
        courselist.drop_course(algo1)
        courselist.drop_course(algo2)
    except:
        pass
    assert courselist.get_credits() == total_credits


def test_length():
    # a new courselist has no courses
    courselist = CourseList()
    assert len(courselist) == 0
    courselist.add_course(isp)
    assert len(courselist) == 1
    courselist.add_course(prog2)
    assert len(courselist) == 2
    courselist.drop_course('01219245')
    assert len(courselist) == 1
    courselist.drop_course('01219999')  # nothing should change
    assert len(courselist) == 1
    courselist.drop_course('01219116')
    assert len(courselist) == 0


if __name__ == '__main__':
    """
    Run the tests by running this file as a Python program.
    This is an alternative to using pytest.
    """
    import traceback
    tests = [test_add_courses, test_drop_course, test_get_credits, test_length]
    failures = 0
    errors = 0
    for testfun in tests:
        try:
            print(testfun.__name__)
            testfun()
        except AssertionError as e:
            print(e)
            failures += 1
        except Exception as e:
            print(traceback.format_exc())
            
            errors += 1
    print(f"Ran {len(tests)} tests, {failures} failed, {errors} errors.")