from util import Queue
class BFS:
    
    def __init__(self, startingTable):
        self.startingState = startingTable
        self.actions = Queue()
        self.actions.push(self.startingState)
        self.visitedNodes = []
        self.stepCount = 0


    def search(self):

        while True:

            self.stepCount += 1
      
            if self.actions.isEmpty():
                print(f"No Solution Found in {self.stepCount} steps")
                break
        
            node = self.actions.pop()
            if node not in self.visitedNodes:
                
                self.visitedNodes.append(node)

                if node.isGoalState():
                    print(f"Solution Found in {self.stepCount} steps")
                    print(node)
                    break

                successorNodes = node.getSuccessors()

                if len(successorNodes) > 0:
                    for successorNode in successorNodes:
                        if successorNode not in self.actions.getStack() and successorNode not in self.visitedNodes:
                            self.actions.push(successorNode)
            else:
                continue

from util import Stack
class DFS:
    
    def __init__(self, startingTable):
        self.startingState = startingTable
        self.actions = Stack()
        self.actions.push(self.startingState)
        self.visitedNodes = []
        self.stepCount = 0


    def search(self):

        while True:

            self.stepCount += 1
      
            if self.actions.isEmpty():
                print(f"No Solution Found in {self.stepCount} steps")
                break
        
            node = self.actions.pop()
            if node not in self.visitedNodes:
                
                self.visitedNodes.append(node)

                if node.isGoalState():
                    print(f"Solution Found in {self.stepCount} steps")
                    print(node)
                    break

                successorNodes = node.getSuccessors()

                if len(successorNodes) > 0:
                    for successorNode in successorNodes:
                        if successorNode not in self.actions.getStack() and successorNode not in self.visitedNodes:
                            self.actions.push(successorNode)
            else:
                continue
                        