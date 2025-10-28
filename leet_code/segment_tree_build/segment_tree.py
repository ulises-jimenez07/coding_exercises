class SegmentTree:
    def __init__(self, data):
        self.tree = [0] * 2 * len(data)
        self.build(data, 0, 0, len(data) -1)
        self.n = len(data)
        print(f"Tree = {self.tree}")

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) //2
            self.build(data, 2*node +1, start, mid)
            self.build(data, 2*node + 2, mid + 1, end)
            self.tree[node] = self.tree[2*node + 1] + self.tree[2*node+2]

    def query(self, l, r, node, start, end):
        if r < start or l > end:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
    
        mid = (start + end) //2
        left_sum = self.query(l,r, 2*node + 1, start, mid)
        right_sum = self.query(l,r, 2*node +2, mid + 1, end)
        return  left_sum + right_sum

    def query_range(self, l,r):
        print(f"Finding answer for range {l} and {r}")
        return self.query(l,r,0,0, self.n-1)

    def update(self, index, updated_value, node, start, end):
        if start == end:
            self.tree[node] = updated_value
        elif start <= index and index <= end:
            mid = (start + end) //2
            if start <= index and index <= mid:
                self.update(index, updated_value, 2*node + 1, start, mid )
            else:
                self.update(index, updated_value , 2*node +2, mid+1, end)
            self.tree[node] = self.tree[2*node +1] + self.tree[2*node +2]

    def update_index(self, index, updated_value):
        self.update(index, updated_value, 0,0, self.n -1)

arr = [2,5,1,6,4,10,8,9]
seg_tree = SegmentTree(arr)

print(seg_tree.query_range(1,5))

seg_tree.update_index(2,9)

print(seg_tree.query_range(1,5))