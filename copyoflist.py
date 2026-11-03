list4=[7,5,9,8]
copylist=list4.copy()

print("copy of list:=",copylist)

#combine 2 lists
list5=[3,4,26,1]
listcombine=list4+list5
print("print the 2 list in combine=",listcombine)

##print in ascending order
listcombine.sort()
print("print the 2 list in ascending order=",listcombine)

##print in descending order
listcombine.sort(reverse=True)
print("print the 2 list in descending order=",listcombine)
