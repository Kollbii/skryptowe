class TermError(Exception):
    '''Raised when user inserts wrong hour, minute or duration.'''
    def __init__(self, message):
        self.message = message