#region imports
from Dice import rollDice
#endregion
from Dice import rollDice
#region functions
def main():  # main function to roll nDice fair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: nothing
    """
    nDice =3 # number of dice
    nMinScore = nDice #  # total score if each die scores 1
    nMaxScore = 6 * nDice# $JES MISSING CODE  # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore + 1# $JES MISSING CODE  # number of possible scores
    nTally = [0] * nNumScores# $JES MISSING CODE  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000# $JES MISSING CODE  # how many times to roll the dice
    for i in range(nRolls):  # each loop rolls dice and increments a score
        total = rollDice(N=nDice)  # call with N=nDice
        nTally[total - nMinScore] += 1  # increment score-nMinScore item b/c 0 indexing start
    print(f"After Rolling {nDice} fair dice {nRolls} times:")
    for i in range(nNumScores):  # print the fraction of rolls for each score
        print(f"Probability of rolling a {i+ nMinScore} : {nTally[i] / nRolls: .4f}")

from Dice import rollUnFairDice

def main2():  # main function to roll nDice unfair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: nothing
    """
    nDice = 3  # number of dice
    nMinScore = nDice  # total score if each die scores 1
    nMaxScore = 6 * nDice# $JES MISSING CODE  # total score if each die scores 6
    nNumScores = nMaxScore - nMinScore + 1# $JES MISSING CODE  # number of possible scores
    nTally = [0] * nNumScores# $JES MISSING CODE  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000# $JES MISSING CODE  # how many times to roll the dice
    for i in range(nRolls):  # each loop rolls dice and increments a score
        total = rollUnFairDice(N=nDice)  # call with N=nDice
        if nMinScore <= total <= nMaxScore:
            nTally[total - nMinScore] += 1# increment score-nMinScore item b/c 0 indexing start
        else:
            print(f"Invalid total: {total}")

    print(f"After {nRolls} rolls of {nDice} dice...")
    for i in range(nNumScores):  # print the fraction of rolls for each score
        print(f"Probability of rolling a {i+ nMinScore} : {nTally[i] / nRolls: .4f}")
#endregion

#this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    main2()