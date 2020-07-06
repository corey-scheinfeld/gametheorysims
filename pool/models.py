from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'pool'
    players_per_group = 8
    num_rounds = 5

    endowment = c(20)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    group_pot = models.CurrencyField()



class Player(BasePlayer):
    sent_tokens = models.CurrencyField()
    private_tokens = models.CurrencyField()
    recieved_tokens = models.CurrencyField()
