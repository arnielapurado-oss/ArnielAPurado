"""ITECC04 Laboratory 4, Part D: the circular queue and the deque.

This part is on your own. No guided walkthrough, and the tests are the only
feedback you get, exactly as in the coding quiz.

WHY CIRCULAR. A queue over a plain list, dequeuing with pop(0), shifts every
remaining element one place left. That is O(n) for an operation that should
be O(1). Moving the FRONT INDEX forward instead of moving the data is the
whole idea, and the modulo operator is what makes the index wrap back to 0
when it runs off the end.

The queue holds a fixed number of slots. It does not grow.
"""


class CircularQueue:

    def __init__(self, capacity):
         if capacity < 1:
             raise ValueError("capacity must be at least 1")
         self._items = [None] * capacity
         self._front = 0
         self._count = 0
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("enqueue on a full queue")
        back = (self._front + self._count) % len(self._items)
        self._items[back] = item
        self._count += 1

    def dequeue(self):
      
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % len(self._items)
        self._count -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self._items[self._front]

    def is_empty(self):
        
        return self._count == 0

    def is_full(self):
        
        return self._count == len(self._items)

    def size(self):
        
        return self._count

    def slots(self):
        """Written for you. Returns a copy of the raw list.

        For inspecting wraparound during the demonstration. Not part of the
        ADT, and your other methods must never call it.
        """
        return list(self._items)


class Deque:
    """A queue you may add to and remove from at both ends."""

    def __init__(self):
        
        self._items = []

    def add_front(self, item):
    
        self._items.insert(0, item)

    def add_rear(self, item):
        self._items.append(item)

    def remove_front(self):
        
        if self.is_empty():
            raise IndexError("remove_front from an empty deque")
        return self._items.pop(0)

    def remove_rear(self):
        
        if self.is_empty():
            raise IndexError("remove_rear from an empty deque")
        return self._items.pop()
    def is_empty(self):
        
        return len(self._items) == 0

    def size(self):
        
        return len(self._items)


def is_palindrome(text):
 
    dq = Deque()
    for char in text:
        if char.isalpha():
            dq.add_rear(char.lower())
    while dq.size() > 1:
        if dq.remove_front() != dq.remove_rear():
            return False
    
    return True
