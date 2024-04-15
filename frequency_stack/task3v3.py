'''
V3. Again rewrite.
36/38 testcases :( without []
with [] passed all tests.

Link on task:
https://leetcode.com/problems/maximum-frequency-stack/description/
'''
from collections import deque

class FreqStack:
    '''
    PLEASE WORK!
    '''

    def __init__(self):
        self.frequencies = deque()
        self.elements = deque()
        self.max_freq = 0

    def push(self, val: int) -> None:
        '''
        Push elements to head of stack.
        '''
        self.elements.appendleft(val)
        freq = self.elements.count(val)
        self.frequencies.appendleft(freq)
        self.max_freq = max(self.max_freq, freq)

    def pop(self) -> int:
        '''
        Pops max frequent element.
        '''
        if not self.elements:
            return None
        position = self.frequencies.index(self.max_freq)
        # for pos, el in enumerate(self.elements):
        #     if pos == position:
        #         result = el
        result = self.elements[position]
        self.frequencies.remove(self.max_freq)
        self.elements.remove(result)
        self.max_freq = max(self.frequencies) if self.frequencies else 0
        return result
