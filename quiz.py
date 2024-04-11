import json

def load_questions():
    with open('quiz.json', 'r') as file:
        questions = json.load(file)
    return questions

def display_question(question):
    print(question['question'])
    options_key = 'options' if 'options' in question else 'choices'
    for i, option in enumerate(question[options_key], start=1):
        print(f"{chr(96 + i)}) {option}")


def main():
    questions = load_questions()
    score = 0
    
    for index, question in enumerate(questions, start=1):
        print(f"\nQuestion {index}:")
        display_question(question)
        user_answer = input("Your answer (a, b, c, or d): ").strip().lower()
        
        if 'correct_ans' in question:
            correct_answer = int(question['correct_ans']) - 1
        elif 'answer' in question:
            correct_answer = question['choices'].index(question['answer'].capitalize())
        else:
            print("Error: 'correct_ans' or 'answer' key not found in question.")
            return
        
        if user_answer == chr(97 + correct_answer):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print(f"The correct answer is {chr(97 + correct_answer)}.")

    total_questions = len(questions)
    print(f"\nYour score: {score}/{total_questions}")

if __name__ == "__main__":
    main()
