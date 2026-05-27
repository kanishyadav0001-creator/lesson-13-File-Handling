file = open("codingal.txt","r")
Counter = 0

content = file.read()

Colist = content.split("\n")

for i in Colist:
    if i:
        Counter += 1

print("This is the number of liner in the file")
print(Counter)