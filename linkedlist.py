class Node:

    def __init__(self, value):
        self.value = value
        self.nxt = None

    def __str__(self):
        return f"{self.value}"

class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None


    def get(self, idx):
        current = self.head
        index = 0
        while current is not None:
            if index == idx:
                return current.value
            else:
                current = current.nxt
                index += 1

    def insert_at(self, idx, value):
        current = self.head
        index = 0
        while current is not None:
            if index + 1 == idx:
                new_node = Node(value)
                new_node.nxt = current.nxt
                current.nxt = new_node
                self.size += 1
                break
            else:
                current = current.nxt
                index += 1

    def insert(self, value):
        if self.size == 0:
            self.head = Node(value)
            self.size += 1
        else:
            current = self.head
            while current is not None:
                if current.nxt is None:
                    current.nxt = Node(value)
                    self.size += 1
                    break
                else:
                    current = current.nxt

    def __str__(self):
        list_str = ""
        current = self.head

        while current:
            if current.nxt is not None:
                list_str += f"{current.value} => "
            else:
                list_str += f"{current.value}"

            current = current.nxt

        return list_str

