from unittest import TestCase

from pyds.deque.listdeque import ListDeque
from pyds.deque.test.mixins import DequeTestMixin


class TestListDeque(TestCase, DequeTestMixin):
    DequeCls = ListDeque
