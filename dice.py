import random

def roll_dice(n):
    results = {}
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        if dice_sum in results:
            results[dice_sum] += 1
        else:
            results[dice_sum] = 1
    i += 1
    return results


 
n = int(input("Enter the number of times to roll the dice: "))
results = roll_dice(n)
print(results)
