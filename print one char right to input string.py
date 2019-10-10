res=[]
def split(str1): 
    return list(str1)
str1=input("Enter letters: ")
sep=split(str1)
for x in sep:
  res.append(chr(ord(x)+1))
for x in res:
  print(x, end='')

#another method using dictionary
''' 
kv = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
res=[]
res1=[]
def split(str1): 
    return list(str1)
str1=input("Enter letters: ")
sep=split(str1)
for x in sep:
  res.append(kv[x])
for x in res:
  res1.append(x+1)
for x in res1:
  print((list(kv.keys())[list(kv.values()).index(x)]) , end="")
'''
