from typing import Any


class ListDeque:
    def __init__(self) -> None:
        self._L = []

    def addfirst(self, item: Any):
        self._L.insert(0, item)

    def addlast(self, item: Any):
        self._L.append(item)

    def removefirst(self):
        return self._L.pop(0)

    def removelast(self):
        return self._L.pop()

    def len(self):
        return len(self._L)
