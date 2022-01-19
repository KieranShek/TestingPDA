import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_1 = Card("Hearts", 3)
        self.card_2 = Card("Diamond", 7)
        self.card_list = [self.card_1, self.card_2]

    def test_card_is_ace(self):
        self.assertEqual(False, CardGame.check_for_ace(self, self.card_1))

    def test_find_highest_card(self):
        self.assertEqual(self.card_2, CardGame.highest_card(self, self.card_1, self.card_2))

    def test_cards_total(self):
        self.assertEqual("You have a total of 10", CardGame.cards_total(self, self.card_list))


