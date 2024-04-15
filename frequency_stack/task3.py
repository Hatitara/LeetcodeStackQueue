'''
Link on task:
https://leetcode.com/problems/maximum-frequency-stack/description/

Medium version, though first done.
For final answer check task3v3.py
'''
from collections import deque

class FreqStack:

    def __init__(self):
        self.stack = deque()

    @property
    def advanced_info(self):
        '''
        Creates better representation to work
        with frequencies.
        '''
        result = deque()
        for k in set(self.stack):
            info = deque()
            info.append(k)
            info.append(self.stack.count(k))
            result.append(info)
        return result

    def __repr__(self) -> str:
        return f'{self.stack}'

    def push(self, val: int) -> None:
        '''
        Adds an element to stack.
        '''
        self.stack.append(val)

    def pop(self) -> int:
        '''
        Pop the most frequent element from the stack.
        '''
        # ChatGPT: Так, ви праві. Set не відноситься до структур даних з довільним доступом.
        no_reps = set(self.stack)
        max_repeat = max(self.stack.count(k) for k in no_reps)
        repeated_max = {k for k in no_reps if self.stack.count(k) == max_repeat}
        self.stack.reverse()
        for k in self.stack:
            if k in repeated_max:
                element = k
                break
        self.stack.remove(element)
        self.stack.reverse()
        return element


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
print()
