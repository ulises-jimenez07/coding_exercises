class SegmentTree:
    def __init__(self, data):
        self.tree = [0] * 2 * len(data)
        self.build(data, 0, 0, len(data) -1)
        print(f"Tree = {self.tree}")

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) //2
            self.build(data, 2*node +1, start, mid)
            self.build(data, 2*node + 2, mid + 1, end)
            self.tree[node] = self.tree[2*node + 1] + self.tree[2*node+2]

arr = [2,5,1,6,4,10,8,9]
seg_tree = SegmentTree(arr)
