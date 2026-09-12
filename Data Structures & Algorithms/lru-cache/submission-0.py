class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):

        self.capacity = capacity

        # HashMap: key -> node
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Initially:
        # left <-> right
        self.left.next = self.right
        self.right.prev = self.left


    # Remove a node from the linked list
    def remove(self, node):

        previous = node.prev
        next_node = node.next

        previous.next = next_node
        next_node.prev = previous


    # Insert a node at the right side
    # Right side = Most Recently Used
    def insert(self, node):

        previous = self.right.prev
        next_node = self.right

        previous.next = node
        next_node.prev = node

        node.prev = previous
        node.next = next_node


    def get(self, key):

        # Key does not exist
        if key not in self.cache:
            return -1

        # Get the node from HashMap
        node = self.cache[key]

        # Move it to Most Recently Used position
        self.remove(node)
        self.insert(node)

        return node.value


    def put(self, key, value):

        # If key already exists,
        # remove the old node first
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)

        # Put it in HashMap
        self.cache[key] = node

        # Put it at Most Recently Used position
        self.insert(node)

        # If capacity exceeded
        if len(self.cache) > self.capacity:

            # Left.next = Least Recently Used node
            lru = self.left.next

            # Remove from linked list
            self.remove(lru)

            # Remove from HashMap
            del self.cache[lru.key]