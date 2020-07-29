from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'condorcet'
    players_per_group = 3
    num_rounds = 10

    instructions_template1 = 'condorcet/instructions.html'
    instructions_template2 = 'condorcet/instructions2.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    jar = models.BooleanField()


class Player(BasePlayer):
    my_hidden_input = models.BooleanField()
