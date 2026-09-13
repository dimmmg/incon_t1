# quotes.py
import random

QUOTES = [
    "Код работает — не трогай.",
    "Семь раз отмерь, один раз запушь в main.",
    "Работает на моем компьютере."
]

def get_random_quote():
    return random.choice(QUOTES)

if __name__ == "__main__":
    print(get_random_quote())