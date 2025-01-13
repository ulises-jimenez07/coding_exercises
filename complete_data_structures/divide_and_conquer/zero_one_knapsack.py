class Item:
    def __init__(self, profit, weight):
        self.weight = weight
        self.profit = profit


def knap_sack_method(items, capacity, current_index):
    if capacity <= 0 or current_index >= len(items):
        return 0
    if items[current_index].weight <= capacity:
        profit1 = items[current_index].profit + knap_sack_method(
            items, capacity - items[current_index].weight, current_index + 1
        )
        profir2 = knap_sack_method(items, capacity, current_index + 1)
        return max(profit1, profir2)
    return 0


mango = Item(31, 3)
apple = Item(26, 1)
orange = Item(17, 2)
banana = Item(72, 5)

items = [mango, apple, orange, banana]

print(knap_sack_method(items, 7, 0))
