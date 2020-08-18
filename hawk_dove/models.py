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
    pass

class Player(BasePlayer):
    choice = models.BooleanField()
    partner_choice = models.BooleanField()
    def set_payoffs(self):
        group = self.get_others_in_group()
        for player in group:
            self.partner_choice = player.choice
            if player.choice == True && self.choice == True:
                player.payoff = 1.5
                self.payoff = 1.5
            if player.choice == True && self.choice == False:
                player.payoff = 0
                self.payoff = 3
            if player.choice == False && self.choice == False:
                player.payoff = -1
                self.payoff = -1
            if player.choice == False && self.choice == True:
                player.payoff = 0
                self.payoff = 3
