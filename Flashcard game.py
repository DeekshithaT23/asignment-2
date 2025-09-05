import json
import random
def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)
data = load_questions("C:\\Users\\deeks\\questions.json")    
def run_quiz(questions):
    score = 0
    question_count = 0
    
    while question_count < 10:
        question = random.choice(questions)
        print(f"\n{question['question']}")
        print("A:", question['options'][0])
        print("B:", question['options'][1])
        print("C:", question['options'][2])
        print("D:", question['options'][3])
        
        answer = input("Your answer (A/B/C/D) or type 'exit' to quit: ").strip().upper()
        
        if answer == 'EXIT' :
            break
        if answer in ['A', 'B', 'C', 'D']:
            if question['options'][ord(answer) - 65] == question['correct_answer']:
                print("Correct!")
                score += 1     
            else:
                print(f"Incorrect! The correct answer was: {question['correct_answer']}")
            question_count += 1
        else:
            print("Invalid input. Please enter A, B, C, D or 'exit'.")
    print(f"\nYour final score is: {score}/{question_count}")

def main():
    questions = load_questions('questions.json')
    run_quiz(questions)

if __name__ == "__main__":
    main()