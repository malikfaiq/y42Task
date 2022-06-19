from .exceptions import NullElementException, EmptyStackException

# Create your models here.

"""
    Stack Class defined with all the feature stack provides.

    Raises:
        NullElementException: raises if the element to be push is None or empty.
        EmptyStackException: raises if the stack is empty or does not have any element in it.

"""


class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        if value:
            self.data.append(value)
        else:
            raise NullElementException

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            raise EmptyStackException

    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            raise EmptyStackException

    def size(self):
        return len(self.data)

    def empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
