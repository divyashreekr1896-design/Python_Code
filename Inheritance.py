class A:
    a=22
class B(A):
    b=33
class C(B):
    c=44
#print(C.a)
#print(C.b)
#print(C.c)
obj=C()
print(obj.a)
print(obj.b)
print(obj.c)