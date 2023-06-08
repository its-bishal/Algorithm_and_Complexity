# numerical value hash function
def mod(number, cellnumber):
    return number%cellnumber

print(mod(200,24))
print(mod(90,17))


# ASCII value hash function

def modASCII(string, cellnumber):
    sum=0
    for i in string:
         sum=ord(i) #ord returns the unicode value of the given string
    return sum%cellnumber

print(modASCII('ACE',16))
print(modASCII('CHANGE',16))

#collision solving in hash table
def collision(string, cellnum):
    sum=0
    for i in string:
        sum=ord(i)
    if sum!=None:
        sum+=1
    return sum%cellnum

print(collision('ACE',21))
print(collision('CHANGE',21))