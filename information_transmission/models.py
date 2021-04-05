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


doc = """
This is an information transmission game inspired by... 
"""


class Constants(BaseConstants):
    name_in_url = 'information_transmission'
    players_per_group = 2
    num_rounds = 8

    instructions_template1 = 'information_transmission/Instructions.html'
    instructions_template2 = 'information_transmission/Instructions2.html'

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    message = models.IntegerField(
        doc="""Message sent by Player 1""",
        label="Please enter a message from 1 to 9:",
        choices = [1,3,5,7,9 ]
    )
    state = models.IntegerField()

    action = models.IntegerField(doc="""Action taken by Player 2""", min=1, max =9)


    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if self.round_number<5:
            p1.payoff = 110 - 10*(abs(self.state - self.action))**1.4
            p2.payoff = 110 - 10*(abs(self.state - self.action))**1.4
        else:
            p1.payoff = 110 - 10 * (abs(self.state - self.action + 1.2)) ** 1.4
            p2.payoff = 110 - 10 * (abs(self.state - self.action)) ** 1.4

class Player(BasePlayer):
    pass
