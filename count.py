x=input("enter a  string(in small letters only)\n")
y=input("the character to be counted(in small letters only)\n")
count=0

for n in x:
    if n==y:
        count=count + 1
print(count)
