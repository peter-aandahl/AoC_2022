import csv

with open('input02.csv', mode='r') as file:

    inputFile = csv.reader(file)

    #A for Rock, B for Paper, and C for Scissors
    #X for Rock, Y for Paper, and Z for Scissors
    outcomes = {'AX':3, 'AY':6, 'AZ':0,
                'BX':0, 'BY':3, 'BZ':6,
                'CX':6, 'CY':0, 'CZ':3}

    moves = {'X':1, 'Y':2, 'Z':3}

    #X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
    strategy = {'AX': 'AZ', 'AY': 'AX', 'AZ': 'AY',
                'BX': 'BX', 'BY': 'BY', 'BZ': 'BZ',
                'CX': 'CY', 'CY': 'CZ', 'CZ': 'CX' }


    score = 0
    strategy_score = 0

    for lines in inputFile:
        outcome = outcomes[lines[0][0]+lines[0][2]]
        mymove = moves[lines[0][2]]
        score = score + outcome + mymove

        strategic_outcome = strategy[lines[0][0]+lines[0][2]]
        strategic_move = strategy[lines[0][0]+lines[0][2]][1]
        strategic_outcome_value = outcomes[strategic_outcome]
        strategic_move_value = moves[strategic_move]
        strategy_score = strategy_score + strategic_outcome_value + strategic_move_value

    print(score,strategy_score)