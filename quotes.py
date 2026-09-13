# quotes.py
import json
import random
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / "config.json"

QUOTES = {
    "dev": [
        "Код работает — не трогай.",
        "Семь раз отмерь, один раз запушь в main.",
        "Работает на моем компьютере.",
        "Пятница — лучший день для деплоя в прод."
    ],
    "life": [
        "Не откладывай на завтра то, что можно задеплоить сегодня.",
        "Кофе — двигатель прогресса."
    ]
}

def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"default_category": "dev"}

def get_random_quote(category=None):
    config = load_config()
    cat = category or config.get("default_category", "dev")
    return random.choice(QUOTES.get(cat, QUOTES["dev"]))

if __name__ == "__main__":
    cfg = load_config()
    print(f"--- {cfg.get('app_name', 'Quote Generator')} ---")
    print(get_random_quote())