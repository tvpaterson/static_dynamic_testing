class CardGame:

# self wasn't included in the parameter
# missed colon after the if and else statement

  def check_for_ace(self, card):
    if card.value == 1:
      return True
    else:
      return False
   
# typo with def was initially dif. return statement missed beside card1. colons were missing 

  def highest_card(self, card1, card2):
    if card1.value > card2.value:
      return card1
    else:
      return card2
    
# self wasn't included in the parameter. interpolation on string needed
# curly brackets surrounding total was missing. colons were missing.

  def cards_total(self, cards):
    total = 0
    for card in cards:
      total += card.value
    return f"You have a total of {total}"