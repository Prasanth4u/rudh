res=[]
def split(str1): 
    return list(str1)
str1=input("Enter letters: ")
sep=split(str1)
for x in sep:
  res.append(chr(ord(x)+1))
for x in res:
  print(x, end='')
