from typing import Any


class Node:
    def __init__(self, item: Any, next) -> None:
        self.item = item
        self.next = next


class LinkedListDeque:
    def __init__(self) -> None:
        self._head = Node(None, None)

    def addfirst(self, item: Any):
        self._head.next = Node(item, self._head.next)

    def addlast(self, item: Any):
        last_node = self._getlastnode()
        last_node.next = Node(item, None)

    def removefirst(self):
        first_node = self._head.next
        if first_node:
            self._head.next = first_node.next
        return getattr(first_node, "item")

    def removelast(self):
        prev_last = self._getprevlastnode()
        last = prev_last.next
        prev_last.next = None
        return getattr(last, "item")

    def len(self):
        count = 0
        node = self._head.next
        while node:
            count += 1
            node = node.next
        return count

    def _getlastnode(self):
        prev_last_node = self._getprevlastnode()
        return prev_last_node.next or prev_last_node

    def _getprevlastnode(self):
        node = self._head
        while node.next and node.next.next:
            node = node.next
        return node
