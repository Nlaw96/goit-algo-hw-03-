import re

def normalize_phone(phone_number):
    normal_phone = re.sub(r'[^\d+]', "", phone_number).strip()

    if normal_phone.startswith("380"):
        normal_phone = "+" + normal_phone
    elif not normal_phone.startswith("+"):
        normal_phone = "+38" + normal_phone
    
    return normal_phone


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


for num in raw_numbers:
    print(normalize_phone(num))
