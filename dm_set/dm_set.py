from node import Node

class DMSet:
    def __init__(self):
        self.head = None

    def add(self, value):
        if not self.contains(value):
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node

    def remove(self, value):
        current = self.head
        previous = None
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next

    def contains(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def union(self, other):
        result = DMSet()
        current = self.head
        while current:
            result.add(current.value)
            current = current.next
        current = other.head
        while current:
            result.add(current.value)
            current = current.next
        return result

    def intersection(self, other):
        result = DMSet()
        current = self.head
        while current:
            if other.contains(current.value):
                result.add(current.value)
            current = current.next
        return result

    def complement(self, universal_set):
        result = DMSet()
        current = universal_set.head
        while current:
            if not self.contains(current.value):
                result.add(current.value)
            current = current.next
        return result

    def difference(self, other):
        result = DMSet()
        current = self.head
        while current:
            if not other.contains(current.value):
                result.add(current.value)
            current = current.next
        return result

    def symmetric_difference(self, other):
        return self.union(other).difference(self.intersection(other))

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return "{" + ", ".join(map(str, values)) + "}"
