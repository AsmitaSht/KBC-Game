import os
import time
que = [
    ["Who is the father of computer?", "A. Charles Babbage", "B. Blaise Pascal", "C. Howard H. Aiken", "D. John Von Neuman", "A"],
    ["What does CPU stand for?", "A. Central Process Unit", "B. Computer Processing Unit", "C. Central Processing Unit", "D. Control Processing Unit", "C"],
    ["Which of the following is an input device?", "A. Monitor", "B. Printer", "C. Keyboard", "D. Speaker", "C"],
    ["Which of the following is not a programming language?", "A. Python", "B. HTML", "C. Java", "D. MS Word", "D"],
    ["Which of these file extensions is used for Python files?", "A. .java", "B. .py", "C. .html", "D. .exe", "B"]
]

levels = [1000, 2000, 3000, 4000, 5000]

W = "Welcome to KBC"
total = 0

print(W.center(100))

for i in range(len(que)):
    os.system('cls')
    print(W.center(100))
    q = que[i]
    print(f"{q[0]}")
    print(f"{q[1]}             {q[2]}")
    print(f"{q[3]}             {q[4]}")
    
    reply = input("Enter the answer (A/B/C/D): ").strip().upper()

    if reply == q[-1]:
        print("✅ Correct answer!")
        total = levels[i]
        time.sleep(2)
    else:
        print("❌ Wrong answer!")
        time.sleep(2)
        break  # Stop the game after a wrong answer

# Final message
os.system('cls')
if total == 0:
    m = "Better luck next time."
    print(m.center(100))
else:
    s = "🎉 CONGRATULATIONS!!!!"
    print(s.center(100))
    m = "You have won: $" + str(total)
    print(m.center(100))
