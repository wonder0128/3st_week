class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 1. 한 곳에서만 자료를 넣고 뺄 수 있다
# 2. LIFO(Last In First Out) -> 가장 마지막에 넣은 값이 제일 빨리 나옴.

# 맨 위에 있는 값만 알면됨
#   - push 함수에서 맨 위에 값을 넣음
#   - pop 함수에서 맨 위에 값을 뺌
#   - peek 함수에서 맨 위의 값을 확인

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "stack is Empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "stack is Empty"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(4)
print(stack.peek())

stack.push(3)
print(stack.peek())

stack.push(5)
print(stack.peek())

print('---------------------------')
stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())

stack.pop()
print(stack.peek())