# quotes.py
import random

QUOTES = {
    "dev": [
        "Код работает — не трогай.",
        "Семь раз отмерь, один раз запушь в main.",
        "Работает на моем компьютере."
    ],
    "life": [
        "Не откладывай на завтра то, что можно задеплоить сегодня.",
        "Кофе — двигатель прогресса."
    ]
}

def get_random_quote(category="dev"):
    return random.choice(QUOTES.get(category, QUOTES["dev"]))

if __name__ == "__main__":
    print(get_random_quote("life"))