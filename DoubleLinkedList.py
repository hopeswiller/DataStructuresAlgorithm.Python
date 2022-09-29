from LinkedList import Node


class Node(Node):
    def __init__(self, key):
        super().__init__(key)
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self._list = self

    @staticmethod
    def linkNodes(prev: Node, next: Node):
        prev.next = next
        next.prev = prev

    def size(self) -> int:
        count = 0
        current = self._list.head
        while current is not None:
            count += 1
            current = current.next

        return count

    def insert(self, value: int):
        newNode = Node(value)
        # case 1 : if insert at head
        if self._list.head is None:
            self._list.head = newNode
            return self._list

        else:
            current = self._list.head
            while current.next is not None:
                current = current.next

            # reached the tail, so insert
            self.linkNodes(current, newNode)

        return self._list

    def insertAfterByValue(self, afterValue: int, value: int):
        newNode = Node(value)
        nextNode = None

        #  traverse till you get to node to insert after
        current = self._list.head
        while current.next is not None and current.key != afterValue:
            current = current.next

        # node is found then link current node to new node and new node to next node of current node
        if current is not None:
            nextNode = current.next
            self.linkNodes(current, newNode)
            self.linkNodes(newNode, nextNode)
        else:
            print(f"Node of value,{afterValue} Not found")

        return self._list

    def deleteByValue(self, value: int):
        # same scenarios as single linkedlists
        current = self._list.head
        # case 1: when at head node

        if current is not None and current.key == value:
            self._list.head = current.next
            current.next.prev = None
            print("Value deleted")
            return self._list

        # case 2
        while current.next is not None and current.key != value:
            current = current.next

        if current is not None:
            # last node
            if current.next is None:
                current.prev.next = None
                return self._list

            self.linkNodes(current.prev, current.next)
        else:
            print(f"Node of value,{value} Not found")

        return self._list

    def __repr__(self):
        iterator = self._list.head
        items = []
        while iterator is not None:
            items.append(iterator.key)
            iterator = iterator.next

        return f"DoubleLinkedList Items ({self.size()}): {items}"


if __name__ == "__main__":

    l = DoubleLinkedList()

    for i in range(10, 28, 2):
        l.insert(i)

    l.insertAfterByValue(14, 15)
    l.insertAfterByValue(18, 19)
    l.insertAfterByValue(22, 23)
    print(l)

    l.deleteByValue(10)
    l.deleteByValue(26)
    l.deleteByValue(19)
    l.deleteByValue(12)
    # l.deleteByPosition(0)
    # l.deleteByPosition(6)

    print(l)
