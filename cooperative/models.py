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

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def live_auction(self, id_in_group, data):
        if id_in_group == 1:
            self.get_player_by_id(1).keep = int(data[0])
            self.get_player_by_id(1).give = int(data[1])
            return {2: data}
        if id_in_group == 2:
            self.get_player_by_id(2).keep = int(data[0])
            self.get_player_by_id(2).give = int(data[1])
            return {1: data}

class Player(BasePlayer):
    my_page_timeout_seconds = models.IntegerField(initial = 300)
    offer_accepted = models.BooleanField()
    lottery_value = models.FloatField()
    give = models.IntegerField()
    keep = models.IntegerField()
    def set_game(self):
        if self.id_in_group == 1:
            self.lottery_value = 1.25
        if self.id_in_group ==2:
            self.lottery_value = 3.75
