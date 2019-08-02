class Stack:     
     def __init__(self):
         self.depts=[]
     def push(self,dept):
         self.depts.append(dept)
     def pop(self,dept):
         self.depts.remove(ch)
     def sort(self,dept):
       self.depts.sort()
       print(self.depts)
       print(self.depts[0])
s=Stack()

n=int(input("Enter Number of values: "))

for i in range(n):
  a=input("Enter Department: ")
  s.push(a)

print(s.depts)
ch=input("Enter Element to POP: ")
s.pop(ch)

print(s.depts)
a=s.depts
s.sort(a)
