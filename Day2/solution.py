# Part1 : Score Grid
# {
#     "A X": 3+1, "A Y": 6+2, "A Z": 0+3,
#     "B Y": 3+2, "B X": 0+1, "B Z": 6+3,
#     "C Z": 3+3, "C X": 6+1, "C Y": 0+2
# }
# * X Y Z
# A 4 8 3
# B 1 5 9
# C 7 2 6

score_grid = [[4,8,3], [1,5,9], [7,2,6]]
def getTotalScore():
    """Calc Winner Score as Per score guide"""
    elf_turn = { "A": 0, "B": 1, "C": 2 }
    my_turn = { "X": 0, "Y": 1, "Z": 2 }
    score = 0
    with open('./puzzle.txt') as games_list:
        rounds = games_list.read().splitlines()
        for round in rounds:
            # Rock (A,X) < Paper (B,Y) <  Scissor (C,Z)
            score += score_grid[elf_turn[round[0]]][my_turn[round[2]]]
    return score

def getPredictedScore():
    """Calc predicted Winner Score as per score guide"""
    # : X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
    elf_turn = { "A": 0, "B": 1, "C": 2 }
    my_turn = { 
        "Y": lambda elf_round : elf_turn[elf_round], # DRAW
        "Z": lambda elf_round : { "A": 1, "B": 2, "C":0  }[elf_round], #WIN
        "X": lambda elf_round : { "A": 2, "B": 0, "C":1  }[elf_round], #LOSE
     }
    score = 0
    with open('./puzzle.txt') as games_list:
        rounds = games_list.read().splitlines()
        for round in rounds:
            # Rock (A,X) < Paper (B,Y) <  Scissor (C,Z)
            score += score_grid[elf_turn[round[0]]][my_turn[round[2]](round[0])]
    return score

if __name__ == "__main__":
    print("Part1: Total Score as per the score guide ", getTotalScore())
    print("Part2: Score as per prediction ", getPredictedScore())