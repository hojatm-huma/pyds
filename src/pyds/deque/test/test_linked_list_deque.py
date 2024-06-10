from unittest import TestCase

from pyds.deque.linkedlist_deque import LinkedListDeque
from pyds.deque.test.mixins import DequeTestMixin


class TestLinkedListDeque(TestCase, DequeTestMixin):
    DequeCls = LinkedListDeque
