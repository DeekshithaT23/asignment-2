import random

def create_solvable_puzzle():
    while True:
        puzzle = list(range(1, 16)) + [0]
        random.shuffle(puzzle)
        if is_solvable(puzzle):
            return puzzle

def is_solvable(puzzle):
    inversions = count_inversions(puzzle)
    blank_row = puzzle.index(0) // 4
    taxi_cab_distance = sum(abs(blank_row - (i // 4)) + abs((puzzle.index(i) % 4) - (i % 4)) for i in range(1, 16))
    return (inversions + taxi_cab_distance) % 2 == 0

def count_inversions(puzzle):
    inversions = 0
    for i in range(len(puzzle)):
        for j in range(i + 1, len(puzzle)):
            if puzzle[i] != 0 and puzzle[j] != 0 and puzzle[i] > puzzle[j]:
                inversions += 1
    return inversions

def display_puzzle(puzzle):
    for i in range(0, 16, 4):
        row = ' '.join(str(puzzle[j]) if puzzle[j] != 0 else 'x' for j in range(i, i + 4))
        print(row)
    print()

def move(puzzle, direction):
    index = puzzle.index(0)
    if direction == 'up' and index > 3:
        puzzle[index], puzzle[index - 4] = puzzle[index - 4], puzzle[index]
    elif direction == 'down' and index < 12:
        puzzle[index], puzzle[index + 4] = puzzle[index + 4], puzzle[index]
    elif direction == 'left' and index % 4 > 0:
        puzzle[index], puzzle[index - 1] = puzzle[index - 1], puzzle[index]
    elif direction == 'right' and index % 4 < 3:
        puzzle[index], puzzle[index + 1] = puzzle[index + 1], puzzle[index]

def is_solved(puzzle):
    return puzzle == list(range(1, 16)) + [0]

def main():
    puzzle = create_solvable_puzzle()
    moves = 0
    display_puzzle(puzzle)

    while True:
        user_input = input("Enter move (up, down, left, right) or 'exit': ").strip().lower()
        if user_input == 'exit':
            print("Exiting the game.")
            break
        if user_input in ['up', 'down', 'left', 'right']:
            move(puzzle, user_input)
            moves += 1
            display_puzzle(puzzle)
            if is_solved(puzzle):
                print(f"Congratulations! You solved the puzzle in {moves} moves.")
                break
        else:
            print("Invalid input. Please enter 'up', 'down', 'left', 'right' or 'exit'.")

if __name__ == "__main__":
    main()