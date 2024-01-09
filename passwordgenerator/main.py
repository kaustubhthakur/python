import random 
import string

def generate_password(min_len,numbers=True,special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if numbers:
        characters+=digits
    if special_char:
        characters+=special
    pwd = ""
    meet_cri = False
    
    has_num = False
    has_spec=False
    while not meet_cri or len(pwd)<min_len:
        new_char = random.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_num = True
        elif new_char in special:
            has_spec = True

        meet_cri = True
        if numbers:
            meet_cri = has_num
        if special_char:
            meet_cri = meet_cri and has_spec
        
    return pwd;
min_len = int(input("Enter the min length"))
pwd = generate_password(min_len)
print(pwd)