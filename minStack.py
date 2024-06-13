class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_dict = {}
        self.index = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        # if the list is empty then the 0th index is the key in the dict for the val
        self.stack.append(val)
        if self.index == 0:
            self.min_dict[self.index] = val
        else:
            # if not empty, then the index of the most recent value in the list is the key for the val pair
            self.min_dict[self.index] = min(val, self.min_dict[self.index - 1])
        self.index += 1


    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.index -= 1
            del self.min_dict[self.index]
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[len(self.stack)-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        # built-in min function
        if self.stack:
            return min(self.min_dict.values())
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
