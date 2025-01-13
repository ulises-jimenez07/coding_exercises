class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CSLinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += "->"
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index >= self.length:
            raise Exception("Index out of range")
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            raise None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

    def delete_by_value(self, value):
        if self.length == 0:
            return False

        if self.head == self.tail and self.head.value == value:
            self.head = None
            self.tail = None
            self.length = 0
            return True

        prev = None
        curr = self.head

        while True:
            if curr.value == value:
                if curr == self.head:
                    self.head = curr.next
                    self.tail.next = self.head
                else:
                    prev.next = curr.next
                    if curr == self.tail:
                        self.tail = prev

                self.length -= 1
                return True

            prev = curr
            curr = curr.next
            if curr == self.head:
                break

        return False

    def split_list(self):
        if self.length == 0:
            return None, None
        first_list = CSLinkedList()
        second_list = CSLinkedList()
        if self.length == 1:
            first_list.append(self.head.value)
            second_list.append(self.head.value)
        else:
            mid = self.length // 2 + self.length % 2
            curr = self.head
            for _ in range(mid):
                first_list.append(curr.value)
                curr = curr.next
            for _ in range(mid, self.length):
                second_list.append(curr.value)
                curr = curr.next

        return first_list, second_list

    def is_sorted(self):
        if self.head is None:
            return True
        curr = self.head
        while curr.next != self.head:
            if curr.data > curr.next.data:
                return False
            curr = curr.next
        return True

    def insert_into_sorted(self, data):
        if self.head == None:
            self.append(data)
        elif data <= self.head.data:
            self.prepend(data)
        else:
            curr = self.head
            while curr.next != self.head and curr.next.data < data:
                curr = curr.next

            new_node = Node(data)
            new_node.next = curr.next
            curr.next = new_node


cslinkded = CSLinkedList()
cslinkded.append(10)
cslinkded.append(20)
cslinkded.append(30)
cslinkded.append(40)
print(cslinkded)
cslinkded.insert(0, 50)
print(cslinkded)
cslinkded.set_value(-1, 100)
print(cslinkded)
cslinkded.pop_first()
print(cslinkded)
