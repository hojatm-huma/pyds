from typing import Any


class ListDeque:
    def __init__(self) -> None:
        self._L = []

    def addfirst(self, item: Any):
        self._L.insert(item)

    def addlast(self, item: Any):
        self.L.append(item)

    def removefirst(self):
        return self._L.pop(0)

    def removelast(self):
        return self._L.pop()
