class Stack():

    def __init__(self):
        self.stack = []

    def push(self,elemnt):
        self.stack.append(elemnt)
    
    def pop(self):
        return self.stack.pop()
    
    def isEmpty(self):
        if(len(self.stack)):
            return False
        return True
    
    def getStack(self):
        return self.stack


class Queue():

    def __init__(self):
        self.stack = []

    def push(self,elemnt):
        self.stack.append(elemnt)
    
    def pop(self):
        return self.stack.pop(0)
    
    def isEmpty(self):
        if(len(self.stack)):
            return False
        return True
    
    def getStack(self):
        return self.stack