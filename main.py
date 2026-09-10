import random


def show_question(question, option_a, option_b, option_c, option_d, correct_answer):
    print("\n" + question)
    print("A. " + option_a)
    print("B. " + option_b)
    print("C. " + option_c)
    print("D. " + option_d)

    while True:
        answer = input("Your answer: ")

        if answer.upper() in ["A", "B", "C", "D"]:
            break

        print("Please enter A, B, C, or D.")

    if answer.upper() == correct_answer:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


def choose_difficulty():
    while True:
        print("\nChoose Difficulty Level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            return "easy"
        elif choice == "2":
            return "medium"
        elif choice == "3":
            return "hard"
        else:
            print("Please enter 1, 2, or 3.")


questions = [
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing User"
        ],
        "answer": "A",
        "difficulty": "easy"
    },
    {
        "question": "Which language is mainly used for web page structure?",
        "options": [
            "Python",
            "HTML",
            "Java",
            "C++"
        ],
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "What does RAM stand for?",
        "options": [
            "Random Access Memory",
            "Read Access Machine",
            "Run Active Memory",
            "Random Application Module"
        ],
        "answer": "A",
        "difficulty": "easy"
    },
    {
        "question": "Which one is a programming language?",
        "options": [
            "Google",
            "Windows",
            "Python",
            "Chrome"
        ],
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "What does URL stand for?",
        "options": [
            "Uniform Resource Locator",
            "Universal Read Link",
            "User Resource Location",
            "Uniform Random Link"
        ],
        "answer": "A",
        "difficulty": "easy"
    },
    {
        "question": "Which data structure uses LIFO?",
        "options": [
            "Queue",
            "Stack",
            "Array",
            "Linked List"
        ],
        "answer": "B",
        "difficulty": "medium"
    },
    {
        "question": "Which HTTP method is commonly used to retrieve data?",
        "options": [
            "POST",
            "DELETE",
            "GET",
            "PUT"
        ],
        "answer": "C",
        "difficulty": "medium"
    },
    {
        "question": "What is the main purpose of an operating system?",
        "options": [
            "To manage computer hardware and software",
            "To create websites",
            "To design images",
            "To browse the internet"
        ],
        "answer": "A",
        "difficulty": "medium"
    },
    {
        "question": "Which concept allows a class to inherit properties from another class?",
        "options": [
            "Encapsulation",
            "Inheritance",
            "Abstraction",
            "Compilation"
        ],
        "answer": "B",
        "difficulty": "medium"
    },
    {
        "question": "Which SQL command is used to retrieve data from a database?",
        "options": [
            "INSERT",
            "UPDATE",
            "SELECT",
            "DELETE"
        ],
        "answer": "C",
        "difficulty": "medium"
    },
    {
        "question": "Which algorithm has an average time complexity of O(n log n)?",
        "options": [
            "Linear Search",
            "Bubble Sort",
            "Merge Sort",
            "Linear Traversal"
        ],
        "answer": "C",
        "difficulty": "hard"
    },
    {
        "question": "What does ACID stand for in database systems?",
        "options": [
            "Atomicity, Consistency, Isolation, Durability",
            "Access, Control, Integration, Data",
            "Automatic, Consistent, Internal, Database",
            "Atomic Control, Information, Data"
        ],
        "answer": "A",
        "difficulty": "hard"
    },
    {
        "question": "Which protocol is mainly used for secure web communication?",
        "options": [
            "HTTP",
            "FTP",
            "HTTPS",
            "SMTP"
        ],
        "answer": "C",
        "difficulty": "hard"
    },
    {
        "question": "Which principle hides internal implementation details from the user?",
        "options": [
            "Inheritance",
            "Polymorphism",
            "Abstraction",
            "Compilation"
        ],
        "answer": "C",
        "difficulty": "hard"
    },
    {
        "question": "Which data structure is commonly used to implement a priority queue?",
        "options": [
            "Heap",
            "Stack",
            "String",
            "Graph"
        ],
        "answer": "A",
        "difficulty": "hard"
    }
]


while True:
    print("\nWelcome to Tech Quiz Game!")

    name = input("Enter your name: ")

    print(f"Hello, {name}! Let's start the quiz.")

    difficulty = choose_difficulty()

    selected_questions = [
        question for question in questions
        if question["difficulty"] == difficulty
    ]

    random.shuffle(selected_questions)

    print(f"\nYou selected: {difficulty.capitalize()}")
    print(f"There are {len(selected_questions)} questions.")

    score = 0

    for question_data in selected_questions:
        score += show_question(
            question_data["question"],
            question_data["options"][0],
            question_data["options"][1],
            question_data["options"][2],
            question_data["options"][3],
            question_data["answer"]
        )

    print("\nQuiz Completed!")
    print(f"Your score: {score}/{len(selected_questions)}")

    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() == "yes":
        print("Starting the quiz again...")
        continue
    else:
        print("Thanks for playing!")
        break