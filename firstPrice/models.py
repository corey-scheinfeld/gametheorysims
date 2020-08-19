from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random as R


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'firstPrice'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_values(self):
        for player in self.get_players():
            player.item_value = R.randint(0, 100)
    def set_payoffs(self):
        highest = 0
        for player in self.get_players():
            if player.bid > highest:
                highest = player.bid
        for player in self.get_players():
            if player.bid == highest:
                player.win = True
                player.payoff = player.item_value - player.bid

class Player(BasePlayer):
    win = models.BooleanField(initial = False)
    bid = models.IntegerField(label = 'Personal Bid:')
    item_value = models.IntegerField()
