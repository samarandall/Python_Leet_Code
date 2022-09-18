class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)
            
    def pop(self) -> int:
        self.stack2 = self.stack1[::-1]
        val = self.stack2.pop()
        self.stack1 = self.stack2[::-1]
        return val

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return not self.stack1
    
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())
print(queue.pop())
print(queue.empty())