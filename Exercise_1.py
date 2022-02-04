"""
Time Complexity: O(1) (For both Push or Pop)
Space Complexity:O(N)

Implement Stack using Array
"""

class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
     def __init__(self):
       self.arr = []
       self.idx = -1
         
     def isEmpty(self):
    	return self.idx == -1
         
     def push(self, item):
       self.idx += 1
       self.arr.insert(self.idx, item)
         
     def pop(self):
        if self.isEmpty():
         return 
        num = self.arr.pop()
        return num
        
     def peek(self):
       if self.isEmpty():
         return
        return self.arr[self.idx]
        
     def size(self):
       return self.idx + 1
         
     def show(self):
       return self.arr
         

s = myStack()
s.push('1')
s.push('2')
print(s.pop())
print(s.show())
