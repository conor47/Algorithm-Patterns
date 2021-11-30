# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2

 

# Constraints:

#     -231 <= val <= 231 - 1
#     Methods pop, top and getMin operations will always be called on non-empty stacks.
#     At most 3 * 104 calls will be made to push, pop, top, and getMin.




# makes use of invariants to retrieve minimum value in O(1) time

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
            return
        current_min = self.stack[-1][1]
        self.stack.append((val,min(val,current_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

# time complexity of each operation is O(1)

# space complexity is O(n)

# An alternative approach would be to use two stacks. One as the main stack and another as the stack for tracking the min values

# Using a linked list would also be an option