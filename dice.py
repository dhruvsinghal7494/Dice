import random

def roll_dice(n):
    results = {7,8,9,10,11,12}
    a = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        if dice_sum in results:
            results[i] = dice_sum
            a += 1
            
    return a;

if __name__ == "__main__":
    n = int(input("Enter the number of times to roll the dice: "))
    a = roll_dice(n)
    #for i in range(7, 12):
        #print(f"Sum {i}: {results.get(i, 0)}")
print(a)

