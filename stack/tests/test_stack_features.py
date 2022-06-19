from django.test import TestCase
from stack.models import Stack
from stack.exceptions import NullElementException, EmptyStackException


"""
    This testing class will test out the impilict and explicit behaviour of stack functionality
    Args:
        TestCase (object): contains predefiend set of features provides by django framework for testing purposes.
"""


class TestStackStructFeatures(TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_stack_push_with_valid_value(self):
        self.stack.push(1)
        self.assertEqual(len(self.stack.data), 1)

    def test_stack_push_with_null_value(self):
        with self.assertRaises(NullElementException):
            self.stack.push(None)

    def test_stack_is_empty(self):
        response = self.stack.empty()
        self.assertEqual(response, True)

    def test_stack_is_not_empty(self):
        self.stack.push(1)
        response = self.stack.empty()
        self.assertEqual(response, False)

    def test_pop_element(self):
        self.stack.push(10)
        response = self.stack.pop()
        self.assertEqual(response, 10)

    def test_pop_on_empty_stack(self):
        with self.assertRaises(EmptyStackException):
            self.stack.pop()

    def test_slack_size(self):
        response = self.stack.size()
        self.assertEqual(response, 0)

    def test_slack_peek(self):
        self.stack.push(1)
        response = self.stack.peek()
        self.assertEqual(response, 1)

    def test_slack_peek_on_empty_stack(self):
        with self.assertRaises(EmptyStackException):
            self.stack.peek()
