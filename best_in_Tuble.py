#LIST[]
l1=[10,20,30]
l2=l1
print(id(l1))
print(id(l2))
l2=list(l1)
print(id(l2))
print(l1==l2)
print(l1 is l2)
print("---------------")
#TUPLE()
t1=[10,20,30]
t2=t1
print(id(t1))
print(id(t2))
l2=list(t1)
print(id(t2))
print(t1==t2)
print(t1 is t2)

