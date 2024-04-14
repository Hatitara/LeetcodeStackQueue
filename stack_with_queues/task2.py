'''
Task link:
https://leetcode.com/problems/implement-stack-using-queues/description/
'''
class Node:
    '''
    Linked list node.
    '''

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def __iter__(self):
        '''
        Iterator method.
        '''
        current = self
        while current:
            yield current
            current = current.next

    def __repr__(self) -> str:
        return f'({self. data}) -> {repr(self.next)}'

    def push(self, node: 'Node'):
        '''
        Pushes one node at the beginning.
        '''
        if isinstance(node, Node):
            node.next = self
            node.next.prev = node
            return node

    def copy(self):
        '''
        Creates a copy of the node.
        '''
        new_node = Node(self.data)
        if self.next:
            new_node.next = self.next.copy()
            new_node.next.prev = new_node
        return new_node

class Queue:
    '''
    Class for queue.
    '''

    def __init__(self) -> None:
        self.head = None

    def __len__(self):
        counter = 0
        if self.head:
            current = self.head
            while current:
                current = current.next
                counter += 1
        return counter

    def __iter__(self):
        if self.head:
            for node in self.head:
                yield node.data

    def __str__(self) -> str:
        if self.head is None:
            return '[]'
        head = '['
        for pos, el in enumerate(self.head):
            if pos:
                head += ', ' + str(el.data)
            else:
                head += str(el.data)
        head += ']'
        return head

    def is_empty(self) -> bool:
        '''
        Checks whether queue is empty.
        '''
        return not bool(self.head)

    def add(self, data):
        '''
        Adds element to the queue end.
        '''
        if self.head:
            self.head = self.head.push(Node(data))
        else:
            self.head = Node(data)

    def pop(self):
        '''
        Removes and returns queue head element.
        '''
        result = None
        if self.head:
            result = self.head.data
            self.head = self.head.next
            if self.head:
                self.head.prev = None
        return result

    def peek(self):
        '''
        Returns queue head element.
        '''
        if self.head:
            return self.head.data
        return None

    def copy(self) -> 'Queue':
        '''
        Returns a copy of queue.
        '''
        result = Queue()
        result.head = self.head.copy() if self.head else None
        return result

class MyStack(object):

    def __init__(self):
        self.default_stack = Queue()
        self.reversed_stack = Queue()

    def __str__(self) -> str:
        return str(self.default_stack)

    def __repr__(self) -> str:
        return str(self)

    def __iter__(self):
        for k in self.default_stack:
            yield k

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.reversed_stack.add(x)
        dummy = self.reversed_stack.copy() if self.reversed_stack else None
        self.default_stack = Queue()
        while dummy and not dummy.is_empty():
            self.default_stack.add(dummy.pop())

    def pop(self):
        """
        :rtype: int
        """
        result = self.reversed_stack.pop()
        dummy = self.reversed_stack.copy() if self.reversed_stack else None
        self.default_stack = Queue()
        while dummy and not dummy.is_empty():
            self.default_stack.add(dummy.pop())
        return result

    def top(self):
        """
        :rtype: int
        """
        return self.reversed_stack.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.default_stack.is_empty() and self.reversed_stack.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# param_3 = obj.top()
# param_2 = obj.pop()
# param_4 = obj.empty()
# print()

# stack = Queue()
# stack.add(5)
# stack.add(7)
# print(f'Check1 - {stack}')
# print(stack.peek(), ' peek1')
# print(stack.pop(), ' pop1')
# print(f'Check2 - {stack}')
# print(stack.peek(), ' peek2')
# stack.add(stack.peek() + 1)
# stack.add(stack.peek() + 2)
# stack.add(stack.peek() + 3)
# stack.add(stack.peek() + 4)
# stack.add(stack.peek() + 5)
# stack.add(stack.peek() + 6)
# print(f'Check3 - {stack}')
