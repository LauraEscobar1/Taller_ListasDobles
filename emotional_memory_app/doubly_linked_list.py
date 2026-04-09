from node import MemoryNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0

    def insert_at_end(self, date, description, emotion):
        new_node = MemoryNode(date, description, emotion)

        if self.head is None:
            self.head = self.tail = self.current = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
        return new_node

    def insert_at_start(self, date, description, emotion):
        new_node = MemoryNode(date, description, emotion)

        if self.head is None:
            self.head = self.tail = self.current = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1
        return new_node


    def delete_node(self, node):
        if not node or self.size == 0:
            return False

        if self.size == 1:
            self.head = self.tail = self.current = None
            self.size = 0
            return True

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        if self.current == node:
            self.current = node.next or node.prev

        self.size -= 1
        return True


    def next(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current
        return None

    def previous(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current
        return None

    def search_by_emotion(self, emotion):
        results = []
        node = self.head

        while node:
            if node.emotion.lower() == emotion.lower():
                results.append(node)
            node = node.next

        return results

    def traverse_forward(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(node)
            node = node.next
        return nodes

    def traverse_backward(self):
        nodes = []
        node = self.tail
        while node:
            nodes.append(node)
            node = node.prev
        return nodes

    def __len__(self):
        return self.size