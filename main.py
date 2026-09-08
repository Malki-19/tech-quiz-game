score = 0
print("welcome to Tech Quiz Game!")
name = input("Enter your name: ")
print(f"Hello, {name}! Let's start the quiz.")
print("\nQuestion 1")
print("What does CPU stand for?")
print("A. central processing unit")
print("B. computer personal unit")
print("C. central program utility")
print("D. control processing user")
answer = input("Your answer : ")
if answer.upper() == "A":
    print("Correct!")
    score += 1
else:
    print("wrong!")
print("\nYour score:", score)