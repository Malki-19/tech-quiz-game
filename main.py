def show_question1():
    print("\nQuestion 1")
    print("What does CPU stand for?")
    print("A. Central Processing Unit")
    print("B. Computer Personal Unit")
    print("C. Central Program Utility")
    print("D. Control Processing User")

    answer = input("Your answer: ")

    if answer.upper() == "A":
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def show_question2():
    print("\nQuestion 2")
    print("Which language is mainly used for web page structure?")
    print("A. Python")
    print("B. HTML")
    print("C. Java")
    print("D. C++")

    answer = input("Your answer: ")

    if answer.upper() == "B":
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def show_question3():
    print("\nQuestion 3")
    print("What does RAM stand for?")
    print("A. Random Access Memory")
    print("B. Read Access Machine")
    print("C. Run Active Memory")
    print("D. Random Application Module")

    answer = input("Your answer: ")

    if answer.upper() == "A":
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def show_question4():
    print("\nQuestion 4")
    print("Which one is a programming language?")
    print("A. Google")
    print("B. Windows")
    print("C. Python")
    print("D. Chrome")

    answer = input("Your answer: ")

    if answer.upper() == "C":
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def show_question5():
    print("\nQuestion 5")
    print("What does URL stand for?")
    print("A. Uniform Resource Locator")
    print("B. Universal Read Link")
    print("C. User Resource Location")
    print("D. Uniform Random Link")

    answer = input("Your answer: ")

    if answer.upper() == "A":
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


while True:
    print("\nWelcome to Tech Quiz Game!")

    name = input("Enter your name: ")

    print(f"Hello, {name}! Let's start the quiz.")

    score = 0

    score += show_question1()
    score += show_question2()
    score += show_question3()
    score += show_question4()
    score += show_question5()

    print("\nQuiz Completed!")
    print(f"Your score: {score}/5")

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() == "yes":
        print("Starting the quiz again...")
        continue
    else:
        print("Thanks for playing!")
        break