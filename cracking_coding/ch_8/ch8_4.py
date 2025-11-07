import copy


def get_subsets(setz, index=None):
    if index is None:
        index = len(setz) - 1
    if index == -1:
        return [[]]

    old_subs = get_subsets(setz, index - 1)
    new_subs = []
    item = setz[index]

    for val in old_subs:
        new_subs.append(val)
        entry = copy.deepcopy(val)
        entry.append(item)
        new_subs.append(entry)
    return new_subs


print(get_subsets([1, 2, 3]))
