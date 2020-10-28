from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyWaitPage(WaitPage):
    group_by_arrival_time = True
    def is_displayed(self):
        return self.round_number == 1

class partisan(Page):
    form_model = 'player'
    form_fields = ['affiliation']
    def is_displayed(self):
        return self.round_number == 1

class GroupWaitPage(WaitPage):
    def is_displayed(self):
         return self.round_number == 1
    after_all_players_arrive = 'adjust_group'

class group_display(Page):
    def is_displayed(self):
         return self.round_number == 1 and (self.group.type == 'pun_partisan' or self.group.type == 'reg_partisan')

class group_display_con(Page):
    def is_displayed(self):
         return self.round_number == 1 and (self.group.type == 'pun_control' or self.group.type == 'reg_control')

class Introduction(Page):
    def is_displayed(self):
         return self.round_number == 1

class NextWait(WaitPage):
    after_all_players_arrive = 'adjust_group'

class contribution(Page):
    form_model = 'player'
    form_fields = ['group_contribution']

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_pot'


class Results1(Page):
    pass

class punishment_partA(Page):
    def is_displayed(self):
        return self.player.label == 'A'
    form_model = 'player'
    def get_form_fields(self):
        if self.group.type == 'pun_partisan' or self.group.type == 'pun_control':
            return ['punishB', 'punishC']
        else:
            return []

class punishment_partB(Page):
    def is_displayed(self):
        return self.player.label == 'B'
    form_model = 'player'
    def get_form_fields(self):
        if self.group.type == 'pun_partisan' or self.group.type == 'pun_control':
            return ['punishA', 'punishC']
        else:
            return []

class punishment_partC(Page):
    def is_displayed(self):
        return self.player.label == 'C'
    form_model = 'player'
    def get_form_fields(self):
        if self.group.type == 'pun_partisan' or self.group.type == 'pun_control':
            return ['punishA', 'punishB']
        else:
            return []

class PunishmentWait(WaitPage):
    def is_displayed(self):
        return self.group.type == 'pun_partisan' or self.group.type == 'pun_control'
    after_all_players_arrive = 'distribute_punishments'

class Results2(Page):
    def is_displayed(self):
        return self.group.type == 'pun_partisan' or self.group.type == 'pun_control'

class FinalWait(WaitPage):
    after_all_players_arrive = 'set_final_payoff'
    def is_displayed(self):
        return self.round_number == 10

class final_results(Page):
    def is_displayed(self):
        return self.round_number == 10


page_sequence = [MyWaitPage, partisan, GroupWaitPage, group_display, group_display_con, Introduction, NextWait, contribution, ResultsWaitPage, Results1, punishment_partA, punishment_partB, punishment_partC, PunishmentWait, Results2, FinalWait, final_results]
