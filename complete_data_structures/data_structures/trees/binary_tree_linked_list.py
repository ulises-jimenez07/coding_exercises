from queue_linked_list import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def pre_order_traversal(root_node):
    """
    Pre-order traversal of binary tree.
    Time complexity: O(n)
    Space complexity: O(n) for recursion stack
    """
    if not root_node:
        return
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node):
    if not root_node:
        return
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)


def post_order_traversal(root_node):
    if not root_node:
        return
    post_order_traversal(root_node.left_child)
    post_order_traversal(root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node):
    if not root_node:
        return
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        print(root.value.data)
        if root.value.left_child is not None:
            custom_queue.enqueue(root.value.left_child)

        if root.value.right_child is not None:
            custom_queue.enqueue(root.value.right_child)


def search_bt(root_node, node_value):
    if not root_node:
        return "The BT does not exist"
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        if root.value.data == node_value:
            return "Success"
        if root.value.left_child is not None:
            custom_queue.enqueue(root.value.left_child)

        if root.value.right_child is not None:
            custom_queue.enqueue(root.value.right_child)
    return "Not Found"


def insert_node_bt(root_node, new_node):
    if not root_node:
        root_node = new_node
    else:
        custom_queue = Queue()
        custom_queue.enqueue(root_node)
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.value.left_child is not None:
                custom_queue.enqueue(root.value.left_child)
            else:
                root.value.left_child = new_node
                return "Sucessfully inserted"
            if root.value.right_child is not None:
                custom_queue.enqueue(root.value.right_child)
            else:
                root.value.right_child = new_node
                return "Sucessfully inserted"


def get_deepest_node(root_node):
    if not root_node:
        return None
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        if root.value.left_child is not None:
            custom_queue.enqueue(root.value.left_child)

        if root.value.right_child is not None:
            custom_queue.enqueue(root.value.right_child)
    deepest_node = root.value
    return deepest_node


def delete_deepest_node(root_node, deepest_node):
    if not root_node:
        return
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        if root.value is deepest_node:
            root.value = None
            return
        if root.value.left_child:
            if root.value.left_child is deepest_node:
                root.value.left_child = None
                return
            custom_queue.enqueue(root.value.left_child)
        if root.value.right_child:
            if root.value.right_child is deepest_node:
                root.value.right_child = None
                return
            custom_queue.enqueue(root.value.right_child)


def delete_node_bt(root_node, node):
    if not root_node:
        return "The BT does not exist"
    custom_queue = Queue()
    custom_queue.enqueue(root_node)
    while not custom_queue.is_empty():
        root = custom_queue.dequeue()
        if root.value.data == node:
            deep_node = get_deepest_node(root_node)
            root.value.data = deep_node.data
            delete_deepest_node(root_node, deep_node)
            return "The node has been deleted"
        if root.value.left_child is not None:
            custom_queue.enqueue(root.value.left_child)
        if root.value.right_child is not None:
            custom_queue.enqueue(root.value.right_child)
    return "Failed to delete"


def delete_bt(root_node):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "The Bt has been sucesfully deleted"


new_bt = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")

new_bt.left_child = cold
new_bt.right_child = hot


tea = TreeNode("Tea")
coffee = TreeNode("coffee")
cola = TreeNode("cola")
fanta = TreeNode("fanta")

cold.left_child = cola
cold.right_child = fanta
hot.left_child = tea
hot.right_child = coffee


# pre_order_traversal(new_bt)
# in_order_traversal(new_bt)
# post_order_traversal(new_bt)
# level_order_traversal(new_bt)

# print(search_bt(new_bt, "Tea"))
# print(search_bt(new_bt, "Hot"))

# new_node = TreeNode("Beer")
# print(insert_node_bt(new_bt, new_node))
# level_order_traversal(new_bt)
# new_node = get_deepest_node(new_bt)
# delete_deepest_node(new_bt, new_node)

# level_order_traversal(new_bt)

delete_node_bt(new_bt, "coffee")
level_order_traversal(new_bt)
