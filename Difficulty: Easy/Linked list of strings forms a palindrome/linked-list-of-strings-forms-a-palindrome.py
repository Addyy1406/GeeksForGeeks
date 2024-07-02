# Back-end complete function Template for Python 3

# Function to compute and check if the given linked list is a palindrome
def compute(h):
    s = ''
    # Iterating through the linked list and adding the data to a string
    while h:
        s += h.data
        h = h.next
    # Checking if the string is equal to its reverse, indicating it is a palindrome
    return s == s[::-1]


# Function to print the elements of the linked list
def printList(head):
    # Iterating through the linked list and printing the data
    while head:
        print(head.data, end=' ')
        head = head.next
#{ 
 # Driver Code Starts
#Initial Template for Python 3


#contributed by RavinderSinghPB
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:

    def __init__(self):
        self.head = None

    def insert(self, data, tail):
        node = Node(data)

        if not self.head:
            self.head = node
            return node

        tail.next = node
        return node


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n1 = int(input())
        arr1 = input().split()
        ll1 = Llist()
        tail = None
        for nodeData in arr1:
            tail = ll1.insert(nodeData, tail)

        if compute(ll1.head):
            print('true')
        else:
            print('false')

# } Driver Code Ends