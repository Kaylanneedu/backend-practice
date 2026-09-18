def parity(answer):
    return "The number is even." if answer % 2 == 0 else "The number is odd."

def n_range(answer):
    if 1 <= answer <= 25:
        return "The number is between 1 and 25"
    
    elif 26 <= answer <= 50:
            return "The number is between 26 and 50"

    elif 51 <= answer <= 75:
            return "The number is between 51 and 75"

    elif 76 <= answer <= 100:
            return "The number is between 76 and 100"

def divisible(answer):
    for n in [3,5,7]:
        if answer % n == 0:
            return f"The number is divisible by {n}."
    return "The number is not divisible by 3, 5, or 7."

hints = [parity, n_range, divisible]