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
Stag Hunt
"""


class Constants(BaseConstants):
    name_in_url = 'staghunt'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'staghunt/instructions.html'



class Subsession(BaseSubsession):
    def creating_session(subsession):
        subsession.group_randomly()


class Group(BaseGroup):
    def set_payoffs(self):
        group = self.get_players()
        player1 = group[0]
        player2 = group[1]
        player1.partner_choice = player2.choice
        player2.partner_choice = player1.choice
        if player1.choice == True and player2.choice == True:
            player1.payoff = 75
            player2.payoff = 75
        if player1.choice == True and player2.choice == False:
            player1.payoff = 0
            player2.payoff = 60
        if player1.choice == False and player2.choice == False:
            player1.payoff = 60
            player2.payoff = 60
        if player1.choice == False and player2.choice == True:
            player1.payoff = 60
            player2.payoff = 0

class Player(BasePlayer):
    choice = models.BooleanField()
    partner_choice = models.BooleanField()
