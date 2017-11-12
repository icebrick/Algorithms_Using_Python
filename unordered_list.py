class Node:
    '''Basic building block for linked list'''
    def __init__(self, init_value):
        self.data = init_value
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        items_list = list()
        current_node = self.head
        while current_node is not None:
            items_list.append(str(current_node.get_data()))
            current_node = current_node.get_next()
        return '[' + ','.join(items_list) + ']'

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def remove(self, item):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            if current_node.get_data() == item:  # Found the node need to remove
                if previous_node is None:  # The node needed to remove is in head
                    self.head = current_node.get_next()
                    current_node.set_next(None)
                else:
                    previous_node.set_next(current_node.get_next())
                    current_node.set_next(None)
                break
            previous_node = current_node
            current_node = current_node.get_next()

    def search(self, item):
        current_node = self.head
        while current_node is not None:
            if current_node.get_data() == item:
                return True
            current_node = current_node.get_next()
        return False

    def is_empty(self):
        return self.head == None

    def size(self):
        current_node = self.head
        counter = 0
        while current_node is not None:
            counter = counter + 1
            current_node = current_node.get_next()
        return counter

    def append(self, item):
        current_node = self.head
        while current_node.get_next() is not None:
            current_node = current_node.get_next()
        new_node = Node(item)
        current_node.set_next(new_node)

    def index(self, item):
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.get_data() == item:
                break
            current_node = current_node.get_next()
            index = index + 1
        return index

    # TODO: fix the bug when pos equal to size of list
    def insert(self, pos, item):
        new_node = Node(item)
        current_node = self.head
        if pos == 0:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            for index in range(pos-2):  # get the node one before the position needed to be inserted
                current_node = current_node.get_next()
            new_node.set_next(current_node.get_next())
            current_node.set_next(new_node)

    def pop(self, pos=None):
        if pos == None:
            pos = self.size() -1
        previous_node = None
        current_node = self.head
        for index in range(pos):
            previous_node = current_node
            current_node = current_node.get_next()
        if previous_node is None: # If the list has only one item
            self.head = current_node.get_next()
        else:
            previous_node.set_next(current_node.get_next())
        pop_item = current_node.get_data()
        return pop_item



li = UnorderedList()


