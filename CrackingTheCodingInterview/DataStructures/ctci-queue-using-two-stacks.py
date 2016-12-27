class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def peek(self):
        if len(self.stack1) == 0:
            self.__reverse(self.stack2, self.stack1)
        el = self.stack1.pop()
        self.stack1.append(el)
        return el

    def pop(self):
        if len(self.stack1) == 0:
            self.__reverse(self.stack2, self.stack1)
        el = self.stack1.pop()
        return el

    def __reverse(self, from_, to):
        while len(from_) > 0:
            to.append(from_.pop())

    def put(self, value):
        self.stack2.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
