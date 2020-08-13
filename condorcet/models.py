from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random as R

author = 'Corey Scheinfeld'

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
    blue_votes = models.IntegerField()
    red_votes = models.IntegerField()
    jar = models.IntegerField(initial = 0)
    jar_type = models.StringField()
    group_decision = models.StringField()
    def create_jar(self):
        self.jar = R.randint(1, 2)
        if(self.jar == 1):
            self.jar_type = 'True'
        if(self.jar == 2):
            self.jar_type = 'False'
    def count_votes(self):
        players = self.get_players()
        for p in players:
            if p.choice == True:
                self.blue_votes = self.blue_votes + 1
            else:
                self.red_votes = self.red_votes + 1
    def part1_decision(self):
        if self.blue_votes > self.red_votes:
            self.group_decision = 'True'
        else:
            self.group_decision = 'False'
    def part2_decision(self):
        if self.blue_votes > 0:
            self.group_decision = 'True'
        else:
            self.group_decision = 'False'
    def set_payoffs(self):
        players = self.get_players()
        for p in players:
            if self.group_decision == self.jar_type:
                p.payoff = 100
            else:
                p.payoff = 10




class Player(BasePlayer):
    choice = models.BooleanField()
