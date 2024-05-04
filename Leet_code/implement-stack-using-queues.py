from collections import deque
class MyStack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
        self.top_element = None

    def push(self, x: int) -> None:
        self.top_element = x
        self.queue2.append(x)

        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        popped = self.queue1.popleft()
        if self.queue1:
            self.top_element = self.queue1[0]
        return popped


    def top(self) -> int:
        return self.top_element
       

    def empty(self) -> bool:
        return not self.queue1
        


