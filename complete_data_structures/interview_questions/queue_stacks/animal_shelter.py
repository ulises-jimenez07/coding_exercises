class AnimalShelter:
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == "cat":
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeue_cat(self):
        if len(self.cats) == 0:
            return None
        cat = self.cats.pop(0)
        return cat

    def dequeue_dog(self):
        if len(self.dogs) == 0:
            return None
        dog = self.dogs.pop(0)
        return dog

    def dequeue_any(self):
        if len(self.cats) == 0:
            return self.dogs.pop(0)
        return self.cats.pop(0)


custom_queue = AnimalShelter()
custom_queue.enqueue("Cat1", "cat")
custom_queue.enqueue("Cat2", "cat")
custom_queue.enqueue("Cat3", "cat")
custom_queue.enqueue("Cat4", "cat")
custom_queue.enqueue("Dog1", "dog")
custom_queue.enqueue("Dog2", "dog")
custom_queue.enqueue("Dog3", "dog")
custom_queue.enqueue("Dog4", "dog")

print(custom_queue.dequeue_cat())
print(custom_queue.dequeue_dog())
print(custom_queue.dequeue_any())
