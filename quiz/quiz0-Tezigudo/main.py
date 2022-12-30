"""Example of using Course and CourseList."""
from course import Course
from courselist import CourseList

courses = [
    Course('01219243', 'Software Specification & Design', 4),
    Course('01219231', 'Database Systems', 3),
    Course('01219222', 'Computer Systems', 4),
    Course('01219218', 'Algo & Data Structures 2', 3),
    Course('01219117', 'Programming 2 Lab', 1),
    Course('01219217', 'Algo & Data Structures 1', 3),
    Course('01204111', 'Programming for Dummies', 4),
    Course('01219114', 'Programming 1', 3),
    Course('01219116', 'Programming 2', 3)
    ]

def main():
    """
    >>> isp = Course('01219245', 'Individual Software Process', 4) # Credits increased!
    >>> f"ISP has course number {isp.course_id} and now worth {isp.credits} credits!"
    'ISP has course number 01219245 and now worth 4 credits!'
    >>> str(isp)   # string representation
    '01219245 Individual Software Process (4)'
    """
    print("Add some courses to a course list")
    courselist = CourseList()
    for course in courses:
        print("Add", course)
        courselist.add_course(course)
        print


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=1)
    main()