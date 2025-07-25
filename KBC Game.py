'''27 KBC Game'''
import os
que=["Who is the father of computer?"," What does CPU stand for?","Which of the following is an input device?","Which of the following is not a programming language?"," Which of these file extensions is used for Python files?"]
a1=["A.Charles Babbage","B.Blaise Pascal","C.Howard H.Aiken","D.John Von Neuman"]
a2=["A. Central Process Unit","B. Computer Processing Unit","C. Central Processing Unit","D. Control Processing Unit"]
a3=["A. Monitor","B. Printer","C. Keyboard","D. Speaker"]
a4=["A. Python","B. HTML","C. Java","D. MS Word"]
a5=["A. .java","B. .py","C. .html","D. .exe"]
a=[a1,a2,a3,a4,a5]
c=["A","C","C","D","B"]
W="Welcome to KBC"
print(W.center(100))
total=0
for i in range(5):
    os.system('cls')
    print(W.center(100))
    print(que[i])
    for j in range(4):
        print(a[i][j])
    n=input("Enter the option:")
    if(n==c[i]):
        total=total+100
    else:
        break
os.system('cls')
if(total==0):
    m="Better luck next time."
    print(m.center(100))
else:
    s="CONGRATULATION!!!!"
    print(s.center(100))
    m="You have won:$"+str(total)
    print(m.center(100))