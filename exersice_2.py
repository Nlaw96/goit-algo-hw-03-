import random 

def get_numbers_ticket(min, max, quantity):
    lottery_num = set()
    while len(lottery_num) != quantity:
        if min >= 1 and max <= 1000:
            lottery_num.add(random.randint(min, max))
            return sorted(list(lottery_num))
    return list(lottery_num)


    

print(get_numbers_ticket(2, 110, 9))
