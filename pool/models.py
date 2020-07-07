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
    num_ro u nds = 5

    endowme nt = c(20)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    group_pot = models.CurrencyField()



class Player(BasePlayer):
    sent_tokens = models.CurrencyField(min = 0, max = 20)
    private_tokens = models.CurrencyField(min = 0, max = 20)
    recieved_tokens = models.CurrencyField()
