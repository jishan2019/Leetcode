# 946. Validate Stack Sequences
# Stack

# Given two sequences pushed and popped with distinct values, return true if and only
# if this could have been the result of a sequence of push and pop operations on an
# initially empty stack.

def validateStackSequences(self, pushed: 'List[int]', popped: 'List[int]') -> 'bool':
    stack = []
    i = 0
    for num in pushed:
        stack.append(num)
        while stack and stack[-1] == popped[i]:
            stack.pop()
            i += 1
    return i == len(popped)