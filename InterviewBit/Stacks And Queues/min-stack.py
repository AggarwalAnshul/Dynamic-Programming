"""
Min Stack
Asked in:  
Yahoo
Amazon
Adobe
Microsoft
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack? 
A: In this case, return -1.

Q: What should pop do on empty stack? 
A: In this case, nothing. 

Q: What should top() do on empty stack?
A: In this case, return -1


[+]Temporal marker           : About 50 Hours Ago | Friday 20, 2020
[+]Temporal marker untethered: 13:23 Hours | Sunday 22, 2020
[+]Comments                  : Finally solved it, I don't think it was influenced by hint
                                There is still room for improvement
[+]Space Complexity          : O(2N)
[+]Time Complexity           : O(1)
[+]Level                     : MEDIUM
[+]Tread Speed               : Relaxed
[+]LINK                      : https://www.interviewbit.com/problems/nearest-smaller-element
[+] Supplement Sources       : N/A

"""
# ACCEPTED!
# Time: O(1) | #Space: O(2*N)
# The idea was to maintain a stack of minimum elements
# if pushed element is less than the minimum element, push this to min stack
# if pushed element is greater than minimum element,do nothing to min stack
# if popped element is equal to minimum element, pop the min stack
# if popped element is greater than minimum element, do nothing to min stack
class MinStack:
    # @param x, an integer
    stack, aux = [], []

    def push(self, x):
        self.stack.append(x)
        if not self.aux or self.aux[-1] > x:
            self.aux.append(x)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.aux[-1]:
                self.aux.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self):
        if self.aux:
            return self.aux[-1]
        return -1

if __name__ == '__main__':
    stack = MinStack()
    print(stack.getMin())
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(3)
    print(stack.getMin())
    stack.pop()
    print(stack.getMin())
