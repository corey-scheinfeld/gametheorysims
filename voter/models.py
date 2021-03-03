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
    Tie = models.BooleanField(initial = False)

    def set_payoffs(self):
        players = self.get_players()
        player1 = players[0]
        player2 = players[1]
        platforms = [.1, .25, .35, .4, .5, .75, .85]
        player1.opponent_platform = player2.platform
        player2.opponent_platform = player1.platform
        player1.participant.vars['votes'] = []
        player2.participant.vars['votes'] = []
        if(player1.platform == player2.platform):
            self.Tie = True
        for x in range(0, 7):
            plat1 = (10-(10*abs(player1.platform - platforms[x])))
            plat2 = (10-(10*abs(player2.platform - platforms[x])))
            if(plat1 > plat2):
                player1.participant.vars['votes'].append('W')
                player2.participant.vars['votes'].append('L')
            elif (plat2 > plat1):
                player1.participant.vars['votes'].append('L')
                player2.participant.vars['votes'].append('W')
            elif plat1 == plat2:
                choice = R.randint(0, 1)
                if choice == 0:
                    player1.participant.vars['votes'].append('TW')
                    player2.participant.vars['votes'].append('TL')
                if choice == 1:
                    player1.participant.vars['votes'].append('TL')
                    player2.participant.vars['votes'].append('TW')
        player1.votes = len(player1.participant.vars['votes'])
        player2.votes = len(player2.participant.vars['votes'])
        if player1.votes > player2.votes:
            player1.winner = True
            player1.payoff = 100
            player2.payoff = -100
        if player1.votes < player2.votes:
            player2.winner = True
            player2.payoff = 100
            player1.payoff = -100


class Player(BasePlayer):
    voters = models.IntegerField()
    winner = models.BooleanField(initial = False)
    votes = models.IntegerField()
    opponent_platform = models.FloatField()
    platform = models.FloatField(label = "Your Platform: ", min = 0, max = 1)
