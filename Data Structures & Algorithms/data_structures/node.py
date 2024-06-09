# Linked list as a data structure
# Ordered and unordered are two common types of linked list

#
class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    # Unordered type of Node :
    # An array containing unordered nodes
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    # Ordered type of Node:
    # Upon addition, an array would be sorted and nodes would be
    # shifted to make room for an insertion of a new node
    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
        else:
            previous = current

        current = current.get_next()
        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
