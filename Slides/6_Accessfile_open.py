# reading a file
file = open("my_file.txt","r")
#print(file.read())
#print(file.readline())
for line in file :
    print("next line")
    print(line)
file.close()


# writing to a file
value = ('the answer', 42)
s = str(value)
print(s)

with open("write.txt","w") as w :
    w.write(s)

with open("my_file.txt","r") as f:
    print(f.tell())
    print(f.readline())
    print(f.tell())
    f.seek(f.tell() + 2)
    print(f.tell())
    print(f.readline())