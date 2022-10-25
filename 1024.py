
import random
l=list()
偶數=list()
奇數=list()

for i in range(10): #loop 10次 #i is empty
    a = random.randint(1, 5) #
    l.append(a) 

    #print(l)

print(l)

for y in range(10):  #loop 10次 # y is 變數 
    if(l[y] % 2)==0: 
        偶數.append(l[y]) #塞值進list
    #print(偶數)
    else:
        奇數.append(l[y]) #塞值進list
        
print(偶數)
print(奇數)

print("這是偶數",len(偶數))
print("這是奇數",len(奇數))