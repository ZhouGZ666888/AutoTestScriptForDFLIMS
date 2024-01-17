""" failure type exceptions
    these exceptions will mark test as failure
"""


class MyBaseFailure(Exception):
    pass


class ParseTestsFailure(MyBaseFailure):
    pass


class ValidationFailure(MyBaseFailure):
    pass


class ExtractFailure(MyBaseFailure):
    pass


class HttpFailure(MyBaseFailure):
    pass


class LoginFailure(MyBaseFailure):
    pass


""" error type exceptions
    these exceptions will mark test as error
"""

from selenium.common.exceptions import TimeoutException


class MyBaseError(Exception):
    pass


class ElementNotClickable(MyBaseError):
    pass


class FileFormatError(MyBaseError):
    pass


class TimeoutExceptions(TimeoutException):
    pass


class ParamsError(MyBaseError):
    pass


class NotFoundError(MyBaseError):
    pass


class FileNotFound(FileNotFoundError, NotFoundError):
    pass


class FunctionNotFound(NotFoundError):
    pass


class VariableNotFound(NotFoundError):
    pass


class EnvNotFound(NotFoundError):
    pass


class DbNotConnect(MyBaseError):
    pass


class DbExecuteNotFound(MyBaseError):
    pass


class ApiNotFound(NotFoundError):
    pass


class TestcaseNotFound(NotFoundError):
    pass


class SummaryEmpty(MyBaseError):
    """ test result summary data is empty
    """


class ElementNotFound(NotFoundError):
    '''
    test result summary data is not find
    '''
    pass


class ElementNotTextAttr(NotFoundError):
    pass
