from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import math as M
import random as R

author = 'Corey Scheinfeld'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Voter'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'voter/instructions.html'




class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()

class Group(BaseGroup):
    winner = models.StringField()

    def set_payoffs(self):
        players = self.get_players()
        player1 = players[0]
        player2 = players[1]
        votes1 = []
        votes2 = []
        platforms = [.1, .25, .35, .4, .5, .75, .85]
        ideal = []
        players[0].opponent_platform = players[1].platform
        players[1].opponent_platform = players[0].platform
        for(x in range(0, 7)):
            plat1 = (10-(10*abs(player1.platform - platforms[x])))
            plat2 = (10-(10*abs(player2.platform - platforms[x])))
            if(plat1 > plat2):
                votes1.append(1)
            elif (plat2 > plat1):
                votes2.append(1)
        players[0].votes = len(votes1)
        players[1].votes = len(votes2)
        if players[1].votes > players[0].votes:
            players[1].winner = True
            players[1].payoff = 100
            players[0].payoff = -100
        if players[1].votes < players[0].votes:
            players[0].winner = True
            players[1].payoff = -100
            players[0].payoff = 100
        elif player[1].votes == player[0].votes:
            self.winner = "Tie"
            choice = R.randint(0, 1)
            if choice == 0:
                players[0].winner = True
                players[1].payoff = -100
                players[0].payoff = 100
            if choice == 1:
                players[1].winner = True
                players[1].payoff = 100
                players[0].payoff = -100


class Player(BasePlayer):
    winner = models.BooleanField(initial = False)
    votes = models.IntegerField()
    opponent_platform = models.FloatField()
    platform = models.FloatField(label = "Your Platform: ", min = 0, max = 1)
