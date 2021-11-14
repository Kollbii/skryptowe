class LessonError(Exception):
    '''Raised when user inserts wrong timetable, term, name, teacher, year or full_time variable'''
    def __init__(self, message: str):
        self.message = message