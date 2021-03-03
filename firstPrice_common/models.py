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
    name_in_url = 'firstPrice_common'
    num_rounds = 5
    players_per_group = 2

    instructions_template = 'firstPrice_common/instructions.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        group_matrix = []
        players = self.get_players()
        ppg = self.session.config['players_per_group']
        for i in range(0, len(players), ppg):
            group_matrix.append(players[i:i+ppg])
        self.set_group_matrix(group_matrix)


class Group(BaseGroup):
    item_value = models.FloatField(initial = 0)
    def set_values(self):
        for players in self.get_players():
            players.hint = round(R.random(), 3)
            self.item_value += players.hint
        self.item_value = round((self.item_value/2), 3)
    def set_payoffs(self):
        highest = 0
        for player in self.get_players():
            if player.bid > highest:
                highest = player.bid
        for player in self.get_players():
            if player.bid == highest:
                player.win = True
                player.payoff = self.item_value - player.bid

class Player(BasePlayer):
    win = models.BooleanField(initial = False)
    bid = models.FloatField(label = 'Personal Bid:')
    hint = models.FloatField()
