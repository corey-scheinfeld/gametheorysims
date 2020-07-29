from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Corey Scheinfeld'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'cooperative'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'cooperative/instructions.html'
    instructions_template2 = 'cooperative/part2.html'
    auction_template = "cooperative/auction.html"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def live_auction(self, id_in_group, data):
        return{0: 'thanks'}

class Player(BasePlayer):
    lottery_value = models.FloatField()
    give = models.IntegerField(min = 0, max = 100, label = 'Given Tickets')
    keep = models.IntegerField(min = 0, max = 100, label = 'Personal Tickets')
    def set_winnings(self):
        if self.id_in_group == 1:
            self.lottery_value = 1.25
        if self.id_in_group ==2:
            self.lottery_value = 3.75
