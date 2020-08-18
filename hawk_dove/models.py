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


author = 'Corey Scheinfeld'

doc = """
Hawk-Dove Game
"""


class Constants(BaseConstants):
    name_in_url = 'hawk_dove'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'hawk_dove/instructions.html'



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_payoffs(self):
        group = self.get_players()
        player1 = group[0]
        player2 = group[1]
        player1.partner_choice = player2.choice
        player2.partner_choice = player1.choice
        if player1.choice == True and player2.choice == True:
            player1.payoff = 1.5
            player2.payoff = 1.5
        if player1.choice == True and player2.choice == False:
            player1.payoff = 0
            player2.payoff = 3
        if player1.choice == False and player2.choice == False:
            player1.payoff = -1
            player2.payoff = -1
        if player1.choice == False and player2.choice == True:
            player1.payoff = 0
            player2.payoff = 3

class Player(BasePlayer):
    choice = models.BooleanField()
    partner_choice = models.BooleanField()
