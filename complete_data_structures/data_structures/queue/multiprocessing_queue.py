from multiprocessing import Queue

custom_queue: Queue = Queue(maxsize=3)  # type: ignore[type-arg]
print(custom_queue.qsize())
print(custom_queue.empty())
custom_queue.put(1)
custom_queue.put(2)
custom_queue.put(3)
print(custom_queue.full())
print(custom_queue.get())
print(custom_queue.qsize())
print(custom_queue.get())
print(custom_queue.get())
print(custom_queue.empty())
