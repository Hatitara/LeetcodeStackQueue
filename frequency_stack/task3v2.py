'''
- Optimizing?
- No, rewriting)

Still bad try. TOO LONG!
For final answer check task3v3.py
'''
class Node:
    '''
    Linked list node.
    '''

    def __init__(self, data=None) -> None:
        self.data = data
        self.frequency = 1 if data else 0
        self.next = None
        self.prev = None

    @property
    def position(self):
        '''
        Position.
        '''
        if self.data is None:
            return 0
        if not self.prev:
            return 1
        return 1 + self.prev.position

    def __iter__(self):
        '''
        Iterator method.
        '''
        current = self
        while current:
            yield current
            current = current.next

    def __repr__(self) -> str:
        return f'({self. data} x{self.frequency}) -> {repr(self.next)}'

    def copy(self):
        '''
        Creates a copy of the node.
        '''
        new_node = Node(self.data)
        if self.next:
            new_node.next = self.next.copy()
            new_node.next.prev = new_node
        return new_node

    def peek(self):
        '''
        Returns last node.
        '''
        cur_node = self
        while cur_node and cur_node.next:
            cur_node = cur_node.next
        return cur_node

    def append(self, node: 'Node'):
        '''
        Appends 
        '''
        if not isinstance(node, Node):
            return None
        cur_node = self
        addition = 0
        while cur_node and cur_node.next:
            if cur_node.data == node.data:
                addition += 1
            cur_node = cur_node.next
        node.frequency += addition
        cur_node.next = node
        cur_node.next.prev = cur_node
        return None

class FreqStack:
    '''
    Yeap.
    '''

    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        return repr(self.head)

    def push(self, val: int) -> None:
        '''
        Adds element to the end of stack.
        '''
        if not self.head:
            self.head = Node(val)
        else:
            self.head.append(Node(val))

    def pop(self) -> int:
        '''
        Pops the most frequent element otherwise last of them.
        '''
        if not self.head:
            return None
        max_freq = max(node.frequency for node in self.head)
        max_freq_nodes = {node for node in self.head if node.frequency == max_freq}
        max_freq_node = Node()
        for node in max_freq_nodes:
            if node.position > max_freq_node.position:
                max_freq_node = node
        if max_freq_node.prev:
            max_freq_node.prev.next = max_freq_node.next
        if max_freq_node.next:
            max_freq_node.next.prev = max_freq_node.prev
        if max_freq_node == self.head:
            self.head = self.head.next
        return max_freq_node.data






# Your FreqStack object will be instantiated and called as such:
obj = FreqStack()
obj.push(5)
obj.push(7)
obj.push(5)
obj.push(7)
obj.push(4)
obj.push(5)
param_1 = obj.pop()
param_2 = obj.pop()
param_3 = obj.pop()
param_4 = obj.pop()
param_5 = obj.pop()
param_6 = obj.pop()
param_7 = obj.pop()
print()
