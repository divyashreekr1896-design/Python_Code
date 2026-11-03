###even and odd num
list3=[10,12,17,14,25,36]
even=0
odd=0

for num in list3:
    if num % 2==0:
        even=even + 1
    else:
        odd=odd + 1
        
print("print only even num",even)
print("print only odd num",odd)

##reverse the list
print(list3)
list3.reverse()
print(list3)