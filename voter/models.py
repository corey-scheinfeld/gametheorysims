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
        players[0].opponent_platform = players[1].platform
        players[1].opponent_platform = players[0].platform
        if player1.voter_decision1() > player2.voter_decision1(self):
            votes1.append(1)
        elif voter_decision1(platform1) < voter_decision1(platform2):
            votes2.append(1)
        elif voter_decision1(platform1) == voter_decision1(platform2):
            choice = R.randint(0, 1)
            if choice == 0:
                votes1.append(1)
            if choice == 1:
                votes2.append(1)
        if voter_decision2(platform1) > voter_decision2(platform2):
            votes1.append(1)
        elif voter_decision2(platform1) < voter_decision2(platform2):
            votes2.append(1)
        elif voter_decision2(platform1) == voter_decision2(platform2):
            choice = R.randint(0, 1)
            if choice == 0:
                votes1.append(1)
            if choice == 1:
                votes2.append(1)
        if voter_decision3(platform1) > voter_decision3(platform2):
            votes1.append(1)
        elif voter_decision3(platform1) < voter_decision3(platform2):
            votes2.append(1)
        elif voter_decision3(platform1) == voter_decision3(platform2):
            choice = R.randint(0, 1)
            if choice == 0:
                votes1.append(1)
            if choice == 1:
                votes2.append(1)
        if voter_decision4(platform1) > voter_decision4(platform2):
            votes1.append(1)
        elif voter_decision4(platform1) < voter_decision4(platform2):
            votes2.append(1)
        elif voter_decision4(platform1) == voter_decision4(platform2):
            choice = R.randint(0, 1)
            if choice == 0:
                votes1.append(1)
            if choice == 1:
                votes2.append(1)
        if voter_decision5(platform1) > voter_decision5(platform2):
            votes1.append(1)
        elif voter_decision5(platform1) < voter_decision5(platform2):
            votes2.append(1)
        elif voter_decision5(platform1) == voter_decision5(platform2):
            choice = R.randint(0, 1)
            if choice == 0:
                votes1.append(1)
            if choice == 1:
                votes2.append(1)
        if voter_decision6(platform1) > voter_decision6(platform2):
            votes1.append(1)
        elif voter_decision6(platform1) < voter_decision6(platform2):
            votes2.append(1)
        elif voter_decision6(platform1) == voter_decision6(platform2):
            choice = R.randint(0, 1)
            if choice == 0:
                votes1.append(1)
            if choice == 1:
                votes2.append(1)
        if voter_decision7(platform1) > voter_decision7(platform2):
            votes1.append(1)
        elif voter_decision7(platform1) < voter_decision7(platform2):
            votes2.append(1)
        elif voter_decision7(platform1) == voter_decision7(platform2):
            choice = R.randint(0, 1)
            if choice == 0:
                votes1.append(1)
            if choice == 1:
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
        if players[1].votes == players[0].votes:
            self.winner = 'Tie'
            choice = R.randint(0, 1)
            if choice == 0:
                players[1].winner = True
                players[1].payoff = 100
                players[0].payoff = -100
            if choice == 1:
                players[0].winner = True
                players[1].payoff = -100
                players[0].payoff = 100

class Player(BasePlayer):
    winner = models.BooleanField(initial = False)
    votes = models.IntegerField()
    opponent_platform = models.FloatField()
    platform = models.FloatField(label = "Your Platform: ", min = 0, max = 1)
    def vars_for_template(self):
        a = 7 - self.votes
        return dict(a = a)
    def voter_decision1(self):
        return(10-10*M.abs(self.platform - .1))
    def voter_decision2(self):
        return(10-10*M.abs(self.platform - .25))
    def voter_decision3(self):
        return(10-10*M.abs(self.platform - .35))
    def voter_decision4(self):
        return(10-10*M.abs(self.platform - .4))
    def voter_decision5(self):
        return(10-10*M.abs(self.platform - .5))
    def voter_decision6(self):
        return(10-10*M.abs(self.platform - .75))
    def voter_decision7(self):
        return(10-10*M.abs(self.platform - .85))
