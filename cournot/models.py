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


author = 'Your name here'

doc = """
Cournot Oligopoly Game
"""


class Constants(BaseConstants):
    name_in_url = 'cournot'
    players_per_group = 2
    num_rounds = 10
    instructions_template = 'cournot/instructions.html'



class Subsession(BaseSubsession):
    def creating_session(subsession):
        subsession.group_randomly()


class Group(BaseGroup):
    price = models.IntegerField()
    def set_market(self):
        players = self.get_players()
        self.price = 100 - (players[0].produce + players[1].produce)
        for p in players:
            p.opp = p.get_others_in_group().produce
            p.profit = p.produce * (self.price - 10)



class Player(BasePlayer):
    produce = models.IntegerField()
    profit = models.IntegerField()
    opp = models.IntegerField()
