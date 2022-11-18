class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> None:
        return str(self.data)
