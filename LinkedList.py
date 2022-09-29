class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Initialize your key structure here.
        List is empty so head points to null
        """
        self.head = None
        self._list = self

    def size(self) -> int:
        count = 0
        current = self._list.head
        while current is not None:
            count += 1
            current = current.next

        return count

    def insert(self, value: int):
        # if list is empty, then new node becomes head
        # else traverse from head till the last node and point that to the new node

        # create new node
        newNode = Node(value)

        if self._list.head is None:
            self._list.head = newNode
        else:
            tail = self._list.head
            while not (tail.next is None):
                tail = tail.next

            # tail is know so point it to to new node
            tail.next = newNode

        return self._list

    # deletion
    def deleteByValue(self, key: int):
        """Deletion by key or value has two cases:
        case 1 : value is found at head node (change head of list to point to next node of the head node)
        case 2 : value is found in the middle or the last node
            (find previous node of the node being deleted and point that node to the next node of the node being deleted)
        """
        previous = None
        current = self._list.head

        # case 1 : if list not empty and headNode holds the value to be deleted
        if current is not None and current.key == key:
            self._list.head = current.next
            print(f"Node of value,{key} found and deleted")
            return self._list

        # case 2 : traverse from begining till key is found and keeping tabs on previous node
        while current.next is not None and current.key != key:
            previous = current
            current = current.next

        # key is found at this point
        if current is not None:
            previous.next = current.next
            print(f"Node of value,{key} found and deleted")
        else:
            print(f"Node of value,{key} Not found")

        return self._list

    def deleteByPosition(self, position: int):
        """Deletion by position has two cases:
        case 1 : position is zero and found at head node (change head of list to point to next node of the head node)
        case 2 : postion is found in the middle or the last node (0 > p <= size)
            (find previous node of the node being deleted and point that node to the next node of the node being deleted)
        """
        previous = None
        current = self._list.head

        # case 1 : if list not empty and position is zero
        if current is not None and position == 0:
            self._list.head = current.next
            print(f"Node at position,{position} found and deleted")
            return self._list

        # case 2: traverse from begining till you find position
        # if the postion was found then currentNode wont be null
        itr = 0
        while current is not None and position > 0 and position < self.size():

            if itr != position:
                previous = current
                current = current.next
            else:
                print(f"Node at position,{position} found and deleted")
                previous.next = current.next
                break
            itr += 1

        # case 3: when position is greater than size of list
        # if position wasnot found then currentNode should be null
        if current is None:
            print(f"Node at position,{position} Not found")

        return self._list

    def __repr__(self):
        iterator = self._list.head
        size = self.size()
        print(f"LinkedList Items ({size}):[", end=" ")
        while iterator is not None:
            print(iterator.key, end=", ")
            iterator = iterator.next

        print("]")


if __name__ == "__main__":

    l = LinkedList()

    for i in range(10, 52, 2):
        l.insert(i)

    print(l.__repr__())

    l.deleteByValue(10)
    l.deleteByValue(20)
    # l.deleteByPosition(0)
    # l.deleteByPosition(6)

    print(l.__repr__())
