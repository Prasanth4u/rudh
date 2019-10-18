#program to find no.of. repeated numbers in the given integer
#wipro elite national talent hunt
#problem Satment: A transfers data to B.
#to safley transfer this data they use key.
#the key is the no.of.repeated numbers of the message send.
#Input: 1223345
#output:2


def split(str1):
    return list(str1)
str1=input()
li=split(str1)
li1=[]
li2=[]
for i in li:
    if (i not in li1):
        li1.append(i) and li1.remove(i)
    else:
        li2.append(i)
print(len(li2))
