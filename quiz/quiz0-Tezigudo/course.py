class Course():
    def __init__(self, course_id: str, description: str, credits: int):
        if not isinstance(credits, int):
            raise TypeError('Credits must be an integer')
        if description.isspace() or not description:
            raise ValueError(
                'description cannot be empty and cannot be only white space')
        if course_id.isspace() or not course_id:
            raise ValueError(
                'Course ID cannot be empty and cannot be only white space')

        self.__course_id = course_id
        self.__description = description
        self.__credits = credits

    @property
    def course_id(self) -> str:
        """get the course id"""
        return self.__course_id

    @property
    def description(self) -> str:
        """get the course description"""
        return self.__description

    @property
    def credits(self) -> int:
        """get the course credits"""
        return self.__credits

    def __str__(self) -> str:
        return f'{self.course_id} {self.description} ({self.credits})'
    __repr__ = __str__

    def __eq__(self, other) -> bool:
        """check whether two courses are equal"""
        if not isinstance(other, Course):
            return False
        return self.course_id == other.course_id and self.description == other.description and self.credits == other.credits

    def __lt__(self, other) -> bool:  # making sortable
        """check whether one course is less than another by id"""
        return self.course_id < other.course_id
