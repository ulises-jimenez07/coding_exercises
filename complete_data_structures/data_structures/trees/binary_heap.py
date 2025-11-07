class Heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heap_size = 0
        self.max_size = size + 1


def peek_of_heap(root_node):
    if not root_node:
        return
    return root_node.custom_list[1]


def size_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.heap_size


def level_order_traversal(root_node):
    if not root_node:
        return
    for i in range(1, root_node.heap_size + 1):
        print(root_node.custom_list[i])


def heapify_tree_insert(root_node, index, heap_type):
    parent_index = index // 2
    if index <= 1:
        return
    if heap_type == "min":
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)
    elif heap_type == "max":
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_tree_insert(root_node, parent_index, heap_type)


def insert_node(root_node, node_value, heap_type):
    if root_node.heap_size + 1 == root_node.max_size:
        return "The binary heal is Full"
    root_node.custom_list[root_node.heap_size + 1] = node_value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)


def heapify_tree_extract(root_node, index, heap_type):
    left_index = index * 2
    right_index = index * 2 + 1
    swap_child = 0

    if root_node.heap_size < left_index:
        return
    if root_node.heap_size == left_index:
        if heap_type == "min":
            if root_node.custom_list[index] > root_node.custom_list[left_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[left_index]
                root_node.custom_list[left_index] = temp
            return
        if root_node.custom_list[index] < root_node.custom_list[left_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[left_index]
            root_node.custom_list[left_index] = temp
        return

    if heap_type == "min":
        if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
            swap_child = left_index
        else:
            swap_child = right_index
        if root_node.custom_list[index] > root_node.custom_list[swap_child]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[swap_child]
            root_node.custom_list[swap_child] = temp
    else:
        if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
            swap_child = left_index
        else:
            swap_child = right_index
        if root_node.custom_list[index] < root_node.custom_list[swap_child]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[swap_child]
            root_node.custom_list[swap_child] = temp
    heapify_tree_extract(root_node, swap_child, heap_type)


def extract_node(root_node, heap_type):
    if root_node.heap_size == 0:
        return
    extracted_node = root_node.custom_list[1]
    root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
    root_node.custom_list[root_node.heap_size] = None
    root_node.heap_size -= 1
    heapify_tree_extract(root_node, 1, heap_type)
    return extracted_node


def delete_binary_heap(root_node):
    root_node.custom_list = None


new_binary_heap = Heap(5)
insert_node(new_binary_heap, 4, "max")
insert_node(new_binary_heap, 5, "max")
insert_node(new_binary_heap, 2, "max")
insert_node(new_binary_heap, 1, "max")
# deleteEntireBP(new_binary_heap)
# level_order_traversal(new_binary_heap)
extract_node(new_binary_heap, "max")
level_order_traversal(new_binary_heap)
