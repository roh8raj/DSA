# Python code to implement a linked list and traverse its values

class Node:
    """Class to create a node structure for a linked list."""
    def __init__(self, data):
        self.data = data        # Data stored in the node
        self.next = None        # Reference to the next node, initialized to None

# Create nodes with specific values
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# Link nodes together to form the linked list
node1.next = node2  # node1 points to node2
node2.next = node3  # node2 points to node3
node3.next = node4  # node3 points to node4

# Traverse the linked list starting from the first node
current = node1  # Start traversal from node1
while current is not None:
    print(current.data, end=" -> ")
    current = current.next  # Move to the next node

# End the linked list with a 'None' to indicate the end of the list
print("None")
