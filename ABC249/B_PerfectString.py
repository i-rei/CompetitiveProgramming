s = list(input())
A = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
A = A.split(" ")
a = list("qwertyuioplkjhgfdsazxcvbnm")
isA = False
isa = False
for i in s:
    if i in A:
        isA = True
    if i in a:
        isa = True
if not (isA and isa):
    print("No")
    exit()
if len(set(s)) == len(s):
    print("Yes")
else:
    print("No")
