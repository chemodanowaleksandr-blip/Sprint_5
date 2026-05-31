import random  
def generate_random_email(cohort_number="cohort_31"):  
    random_digits = random.randint(100, 999)  
    return f"alexandr_chernov_{cohort_number}_{random_digits}@yandex.ru"  
def generate_random_password(length=6):  
    chars = "abcdefghijklmnopqrstuvwxyzXYZ1234567890"  
    return "".join(random.sample(chars, length))  
