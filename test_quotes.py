# test_quotes.py
import unittest
from quotes import get_random_quote, QUOTES, load_config

class TestQuoteGenerator(unittest.TestCase):

    def test_get_random_quote_dev(self):
        """Проверяем, что возвращается фраза из категории dev"""
        quote = get_random_quote("dev")
        self.assertIn(quote, QUOTES["dev"])

    def test_get_random_quote_life(self):
        """Проверяем, что возвращается фраза из категории life"""
        quote = get_random_quote("life")
        self.assertIn(quote, QUOTES["life"])

    def test_fallback_category(self):
        """Если передана несуществующая категория, должен срабатывать дефолт (dev)"""
        quote = get_random_quote("unknown_category")
        self.assertIn(quote, QUOTES["dev"])

    def test_config_loader(self):
        """Проверяем чтение конфигурации"""
        cfg = load_config()
        self.assertIsInstance(cfg, dict)
        self.assertIn("default_category", cfg)

if __name__ == "__main__":
    unittest.main()