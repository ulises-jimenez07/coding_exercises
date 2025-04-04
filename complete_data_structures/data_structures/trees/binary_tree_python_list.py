class BinaryTree:
    def __init__(self, size):
        self.custom_list = size * [None]
        self.last_used_index = 0
        self.max_size = size

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "The Binary Tree is full"
        self.custom_list[self.last_used_index + 1] = value
        self.last_used_index += 1
        return "The value has been sucessfully added"

    def search_node(self, node_value):
        for item in self.custom_list:
            if item == node_value:
                return "Success"
        return "Not found"

    def pre_order_traversal(self, index):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index * 2)
        self.pre_order_traversal(index * 2 + 1)

    def in_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.in_order_traversal(index * 2)
        print(self.custom_list[index])
        self.in_order_traversal(index * 2 + 1)

    def post_order_traversal(self, index):
        if index > self.last_used_index:
            return
        self.post_order_traversal(index * 2)
        self.post_order_traversal(index * 2 + 1)
        print(self.custom_list[index])

    def level_order_traversal(self, index):
        for i in range(index, self.last_used_index + 1):
            print(self.custom_list[i])

    def delete_node(self, value):
        if self.last_used_index == 0:
            return "There is not node to delete"
        for i in range(1, self.last_used_index + 1):
            if self.custom_list[i] == value:
                self.custom_list[i] = self.custom_list[self.last_used_index]
                self.custom_list[self.last_used_index] = None
                self.last_used_index -= 1
                return "The node has been sucessfully deleted"

    def delete_bt(self):
        return "The BT has been sucessfully deleted"


new_bt = BinaryTree(8)
new_bt.insert_node("Drinks")
new_bt.insert_node("Hot")
new_bt.insert_node("Cold")
new_bt.insert_node("Tea")
new_bt.insert_node("Coffee")


# new_bt.pre_order_traversal(1)
# new_bt.in_order_traversal(1)
# new_bt.post_order_traversal(1)

print(new_bt.delete_node("Cold"))
new_bt.level_order_traversal(1)
