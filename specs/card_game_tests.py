import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card("diamonds", 1)
        self.card2 = Card("hearts", 3)

        self.cardgame = CardGame()


    def test_check_for_ace(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card1))

    def test_highest_card(self):
        highest_card = self.cardgame.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, highest_card)

    def test_cards_total(self):
        card1 = Card("diamonds", 1)
        card2 = Card("hearts", 3)
        cards = [card1, card2]
        self.assertEqual("You have a total of 4", self.cardgame.cards_total(cards))