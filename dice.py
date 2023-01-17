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


# if __name__ == "__main__":
#     n = int(input("Enter the number of times to roll the dice: "))
#     a = roll_dice(n)
#     for i in range(2, 12):
#         #print(f"Sum {i}: {results.get(i, 0)}")
# print(a)

n = int(input("Enter the number of times to roll the dice: "))
print(roll_dice(n))
