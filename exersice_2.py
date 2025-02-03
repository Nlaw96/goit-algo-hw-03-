import random 

def get_numbers_ticket(min, max, quantity):    
    if not (1 <= min <= max <= 1000 and quantity <= (max - min + 1)):
        return []
    lottery_num = random.sample(range(min, max + 1), quantity)
    return sorted(lottery_num)


lottery_numbers = get_numbers_ticket(2, 2000, 9)
print("Ваші лотерейні числа:", lottery_numbers)

