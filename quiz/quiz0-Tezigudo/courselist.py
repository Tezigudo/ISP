class CourseList():
    def __init__(self) -> None:
        self.course_list: dict = {} # dict to store the course

    @property
    def all_course_id(self) -> list:
        """all course id of the course list"""
        return self.course_list.keys()

    def add_course(self, course) -> bool:
        """add course to the course list"""
        if course.course_id in self.all_course_id:
            # check whether the course is already in the course list
            return False
        self.course_list[course.course_id] = course
        return True

    def drop_course(self, course_id: str) -> bool:
        """drop course from the course list"""
        if course_id not in self.all_course_id:
            # check whether the course is in the course list
            return False
        del self.course_list[course_id]
        return True

    def get_credits(self) -> int:
        """get all of the credits of course list"""
        return sum([course.credits for course in self.course_list.values()])

    def get_course(self, course_id: str):
        """get course by id"""
        if course_id not in self.all_course_id:
            # check whether the course is in the course list
            return None
        return self.course_list[course_id]

    def __len__(self) -> int:
        """get the length of the course list"""
        return len(self.course_list)
