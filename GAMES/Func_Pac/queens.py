import itertools
import random

def queens(queens_positions):
    for i in range(len(queens_positions)):
        for j in range(i + 1, len(queens_positions)):
            row1, col1 = queens_positions[i]
            row2, col2 = queens_positions[j]
            if row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                return False
    return True

def generation_successful():
    successful_args = []
    permutations = list(itertools.permutations(range(1, 9)))
    random.shuffle(permutations)

    for permutation in permutations:
        queens_positions = [(i + 1, permutation[i]) for i in range(8)]
        if queens(queens_positions):
            successful_args.append(queens_positions)
            if len(successful_args) == 4:
                break

    return successful_args
