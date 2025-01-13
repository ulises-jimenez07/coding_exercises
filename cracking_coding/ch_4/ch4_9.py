#given a binary tree , print all possible arrays that could have led to the tree

from coding_interview.CrackingCoding.ch_4.binary_search_tree import BinarySearchTree

def find_bst_sequences(bst):
    #mask function to send the root
    if not bst.root:
        return []
    return helper(bst.root)


def helper(node):
    if not node:
        return [[]]
    #recurse through subtress
    right_sequences = helper(node.right)
    left_sequences = helper(node.left)
    sequences = []
    for right in right_sequences:
        for left in left_sequences:
            #weave through sequences
            sequences = weave(left, right, [node.key], sequences)
    return sequences


def weave(first, second, prefix, results):
    # when one list is emputy add remainder to a clined prefix and store resutls
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return results

    #recurse with the head for the first item
    head = first[0]
    prefix.append(head)
    results = weave(first[1:], second, prefix, results)
    prefix.pop()
    #recurse with the head for the second item
    head = second[0]
    prefix.append(head)
    results = weave(first, second[1:], prefix, results)
    prefix.pop()
    return results


bst = BinarySearchTree()
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
# bst.insert(11);
# bst.insert(14);

sequences = find_bst_sequences(bst)
print(sequences)