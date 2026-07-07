class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def dsp(self):
        print(self.items)
    def pop(self):
            if self.item:
                 print("Stack is empty")
            else:
                 return self.items.pop()
    def is_empty(self):
         if len(self.item)==0:
              return True
s1=Stack()
s1.push(10)
s1.push(12)
s1.dsp()