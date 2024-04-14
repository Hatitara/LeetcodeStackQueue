'''
Task link:
https://leetcode.com/problems/implement-queue-using-stacks/
'''
class Node:
    '''
    Linked list node.
    '''

    def __init__(self, data=None, next_el=None) -> None:
        self.data = data
        self.next = next_el

    def __iter__(self):
        '''
        Iterator method.
        '''
        current = self
        while current:
            yield current
            current = current.next

    def __repr__(self) -> str:
        return f'{self. data} -> {repr(self.next)}'

    def push(self, node: 'Node'):
        '''
        Pushes one node at the beginning.
        '''
        if isinstance(node, Node):
            node.next = self
            return node

    def append(self, node: 'Node'):
        '''
        Appends node to the end.
        '''
        if isinstance(node, Node):
            current = self
            while current and current.next:
                current = current.next
            current.next = node

    def copy(self):
        '''
        Creates a copy of the node.
        '''
        new_mono = Node(self.data)
        if self.next:
            new_mono.next = self.next.copy()
        return new_mono

class Stack:
    '''
    My stack implementation using linked list.
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

    def __repr__(self) -> str:
        return str(self)

    def is_empty(self) -> bool:
        '''
        Checks whether stack is empty.
        '''
        return not bool(self.head)

    def push(self, data) -> None:
        '''
        Adds data to the head of stack.
        '''
        new_node = Node(data)
        if self.head:
            self.head = self.head.push(new_node)
        else:
            self.head = new_node

    def pop(self):
        '''
        Removes and return an element from
        head of the stack.
        '''
        if self.head:
            data = self.head.data
            self.head = self.head.next
            return data
        return None

    def peek(self):
        '''
        Returns the top element of the stack.
        '''
        if self.head:
            return self.head.data
        return None

    def copy(self):
        '''
        Returns a copy of stack.
        '''
        new_stack = Stack()
        new_stack.head = self.head.copy()
        return new_stack

class MyQueue:
    '''
    My queue class.
    '''
    def __init__(self):
        self.default_stack = Stack()
        self.reversed_stack = Stack()

    def __str__(self) -> str:
        return str(self.default_stack)

    def __repr__(self) -> str:
        return repr(self.default_stack)

    def __iter__(self):
        for k in self.default_stack:
            yield k

    def push(self, data):
        '''
        Pushes element into the queue end.
        '''
        self.default_stack.push(data)
        dummy = self.default_stack.copy()
        new_stack = Stack()
        while not dummy.is_empty():
            new_stack.push(dummy.pop())
        self.reversed_stack = new_stack

    def pop(self):
        '''
        Pops queue head element.
        '''
        result = self.reversed_stack.pop()
        dummy = self.reversed_stack.copy()
        new_stack = Stack()
        while not dummy.is_empty():
            new_stack.push(dummy.pop())
        self.default_stack = new_stack
        return result

    def peek(self):
        '''
        Peek in queue.
        '''
        return self.reversed_stack.peek()

    def empty(self):
        '''
        Checks whether queue is empty.
        '''
        return self.default_stack.is_empty() and self.reversed_stack.is_empty()



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.push(4)
# obj.push(5)
# obj.pop()
# obj.pop()
# print(obj)
# print(obj.peek())


# stack = Stack()
# stack.push(5)
# stack.push(7)
# print(f'Check1 - {stack}')
# print(stack.peek(), ' peek1')
# print(stack.pop(), ' pop1')
# print(f'Check2 - {stack}')
# print(stack.peek(), ' peek2')
# stack.push(stack.peek() + 1)
# stack.push(stack.peek() + 1)
# stack.push(stack.peek() + 1)
# stack.push(stack.peek() + 1)
# stack.push(stack.peek() + 1)
# stack.push(stack.peek() + 1)
# print(f'Check3 - {stack}')
