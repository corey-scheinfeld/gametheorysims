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
    name_in_url = 'cooperative'
    players_per_group = 2
    num_rounds = 2

    instructions_template = 'cooperative/instructions.html'
    instructions_template2 = 'cooperative/part2.html'

class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()
        groups = self.get_groups()
        for g in groups:
            players = g.get_players()
            for p in players:
                if p.id_in_group == 1:
                    p.lottery_value = 1.25
                if p.id_in_group ==2:
                    p.lottery_value = 3.75


class Group(BaseGroup):
    def live_auction(self, id_in_group, data):
        if data == 'game_finished':
            return {0: data}
        else if id_in_group == 1:
            self.get_player_by_id(1).keep = int(data[0])
            self.get_player_by_id(1).give = int(data[1])
            return {2: data}
        else if id_in_group == 2:
            self.get_player_by_id(2).keep = int(data[0])
            self.get_player_by_id(2).give = int(data[1])
            return {1: data}
    def set_payoff(self):
        players = self.get_players()
        for p in players:
            p.chance = R.randint(1, 100);
            if p.chance <= p.keep:
                p.payoff = p.lottery_value
            else:
                p.payoff = 0


class Player(BasePlayer):
    my_page_timeout_seconds = models.IntegerField(initial = 300)
    offer_accepted = models.BooleanField()
    lottery_value = models.FloatField()
    chance = models.IntegerField()
    give = models.IntegerField()
    keep = models.IntegerField()
