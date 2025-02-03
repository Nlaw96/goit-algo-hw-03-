import random 

def get_numbers_ticket(min, max, quantity):
        if not (1 <= min <= max <= 1000 and quantity <= (max - min + 1)):
        return []

    return sorted(lottery_num = random.sample(range(min, max), quantity))


lottery_numbers = get_numbers_ticket(2, 2000, 9)
print("Ваші лотерейні числа:", lottery_numbers)

