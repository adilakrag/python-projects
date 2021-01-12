print ("HELLO WORLD")
prev = 1
curr = 1
next = 0

i=0
print (curr)
print(prev)
while i <100:
    next = curr + prev
    print(next);
    prev=curr
    curr=next
    i += 1;