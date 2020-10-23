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
         return self.round_number and (self.group.type == 'pun_partisan' or self.group.type == 'pun_control')

class contribution(Page):
    form_model = 'player'
    form_fields = ['group_contribution']


class ResultsWaitPage(WaitPage):
    body_text = """After all group members have arrived, we calculate\n total_contributions = sum(contribution) for all players\n individual_share = 2/3 total_contributions\n\n
    stage 1 payoffs (for each individual) = 20 - contribution + individual_share"""
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

    body_text = """
    Once all group members arrive, we need to calculate:\n
    How much each person spent in total reducing other people’s earnings\m
    How much others spent to reduce their earnings\m
    How much each person had their earnings reduced = (3 x amount others’ spent)\m
    Final payoff for the period = max{0, stage1_payoff - (how much own payoff was reduced)} - amount spent reducing other people’s payoffs"""
    after_all_players_arrive = 'distribute_punishments'

class Results2(Page):
    def is_displayed(self):
        return self.group.type == 'pun_partisan' or self.group.type == 'pun_control'

class FinalWait(WaitPage):
    def is_displayed(self):
        return self.round_number == 10
    after_all_players_arrive = 'set_final_payoff'


class final_results(Page):
    def is_displayed(self):
        return self.round_number == 10


page_sequence = [MyWaitPage, partisan, GroupWaitPage, group_display, contribution, ResultsWaitPage, Results1, punishment_partA, punishment_partB, punishment_partC, PunishmentWait, Results2, final_results]
