
# Game points

ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
DRAW = 30
WIN = 60

'''
PART 1
'''
# CODELIST = {
#     'A': ROCK,
#     'B': PAPER,
#     'C': SCISSORS,
#     'X': ROCK,
#     'Y': PAPER,
#     'Z': SCISSORS
# }

'''
PART 2
'''
CODELIST = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'X': LOSE,
    'Y': DRAW,
    'Z': WIN
}

def get_points_per_rounds(line :str):
    play = line.replace('\n', '').split(' ')

    if len(play) == 2:
        if play[0] in CODELIST.keys():
            if play[1] in CODELIST.keys():
                # return CODELIST[play[1]] + play_game_p1(CODELIST[play[0]], CODELIST[play[1]])
                choice = cheat_play(CODELIST[play[0]], CODELIST[play[1]])
                score = play_game_p1(CODELIST[play[0]], choice) // 10
                score += choice
                return score

    raise Exception("Wrong input format")

'''
Plays game
Returns DRAW, WIN or LOSE from p1's perspective
'''
def play_game_p1(p0, p1):
    if p0 == p1:
        return DRAW
    if p0 == ROCK and p1 == PAPER:
            return WIN
    elif p0 == PAPER and p1 == SCISSORS:
            return WIN
    elif p0 == SCISSORS and p1 == ROCK:
            return WIN
    else:
        return LOSE

'''
According to known input this function returns what is
needed to play for a desired outcome
@Param opponent's choice
@Param desired outcome
@return your choice
'''
def cheat_play(p0, outcome):
    if outcome == DRAW:
        return p0
    else:
        choices = [ROCK, PAPER, SCISSORS]
        choices.remove(p0)
        for choice in choices:
            if outcome == play_game_p1(p0, choice):
                return choice


def main():

    sum = 0

    strategy_guide = open('input.txt')

    for line in strategy_guide.readlines():
        sum += get_points_per_rounds(line)

    strategy_guide.close()

    print(sum)

if __name__ == '__main__':
    main()