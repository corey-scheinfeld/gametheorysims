from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
 import Random as R

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'condorcet'
    players_per_group = 3
    num_rounds = 10

    instructions_template1 = 'condorcet/instructions1.html'
    instructions_template2 = 'condorcet/instructions2.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    jar = models.IntegerField(initial = 0)
    jar_type = models.BooleanField()
    def create_jar(self):
        self.jar = Math.floor(Math.random()*2)+1
        if(self.jar == 1):
            self.jar_type = True
        if(self.jar == 2):
            self.jar_type = False



class Player(BasePlayer):
    my_hidden_input = models.BooleanField()
