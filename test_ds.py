from unittest import TestCase

from linkedlist import LinkedList

class LinkedListTest(TestCase):

    def test_insert(self):
        # Insert element to list
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        ll.insert(4)

        self.assertEqual("1 => 2 => 3 => 4", str(ll))
        self.assertEqual(ll.size, 4)

    def test_insert_at(self):
        # Insert element to list into idx
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        ll.insert(4)

        ll.insert_at(2, 5)

        self.assertEqual("1 => 2 => 5 => 3 => 4", str(ll))

    def test_get(self):
        # Insert element to list into idx
        ll = LinkedList()
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        ll.insert(4)

        value = ll.get(2)

        self.assertEqual(3, value)
