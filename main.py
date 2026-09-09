import random


def show_question(question, option_a, option_b, option_c, option_d, correct_answer):
    print("\n" + question)
    print("A. " + option_a)
    print("B. " + option_b)
    print("C. " + option_c)
    print("D. " + option_d)

    answer = input("Your answer: ")

    if answer.upper() == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


questions = [
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which language is mainly used for web page structure?",
        "options": [
            "Python",
            "HTML",
            "Java",
            "C++"
        ],
        "answer": "B"
    },
    {
        "question": "What does RAM stand for?",
        "options": [
            "Random Access Memory",
            "Read Access Machine",
            "Run Active Memory",
            "Random Application Module"
        ],
        "answer": "A"
    },
    {
        "question": "Which one is a programming language?",
        "options": [
            "Google",
            "Windows",
            "Python",
            "Chrome"
        ],
        "answer": "C"
    },
    {
        "question": "What does URL stand for?",
        "options": [
            "Uniform Resource Locator",
            "Universal Read Link",
            "User Resource Location",
            "Uniform Random Link"
        ],
        "answer": "A"
    }
]


while True:
    print("\nWelcome to Tech Quiz Game!")

    name = input("Enter your name: ")

    print(f"Hello, {name}! Let's start the quiz.")

    score = 0

    random.shuffle(questions)

    for question_data in questions:
        score += show_question(
            question_data["question"],
            question_data["options"][0],
            question_data["options"][1],
            question_data["options"][2],
            question_data["options"][3],
            question_data["answer"]
        )

    print("\nQuiz Completed!")
    print(f"Your score: {score}/{len(questions)}")

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() == "yes":
        print("Starting the quiz again...")
        continue
    else:
        print("Thanks for playing!")
        break