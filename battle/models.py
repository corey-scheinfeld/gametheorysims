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
Battle of the Sexes
"""


class Constants(BaseConstants):
    name_in_url = 'battle'
    players_per_group = 2
    num_rounds = 5

    instructions_template = 'battle/instructions.html'
    row_roll = 'row'
    column_roll = 'column'



class Subsession(BaseSubsession):
    def creating_session(subsession):
        subsession.group_randomly()


class Group(BaseGroup):
    def set_payoffs(self):
        player1 = group.get_player_by_role(Constants.row_roll)
        player2 = group.get_player_by_role(Constants.column_roll)
        player1.partner_choice = player2.choice
        player2.partner_choice = player1.choice
        if player1.choice == True and player2.choice == True:
            player1.payoff = 600
            player2.payoff = 200
        if player1.choice == True and player2.choice == False:
            player1.payoff = 0
            player2.payoff = 0
        if player1.choice == False and player2.choice == False:
            player1.payoff = 200
            player2.payoff = 600
        if player1.choice == False and player2.choice == True:
            player1.payoff = 0
            player2.payoff = 0

class Player(BasePlayer):
    choice = models.BooleanField()
    partner_choice = models.BooleanField()
