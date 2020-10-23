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
    pass

class contribution(Page):
    form_model = 'player'
    form_fields = ['group_contribution']


class ResultsWaitPage(WaitPage):
    body_text = """After all group members have arrived, we calculate\n total_contributions = sum(contribution) for all players\n individual_share = 2/3 total_contributions\n\n
    stage 1 payoffs (for each individual) = 20 - contribution + individual_share"""
    after_all_players_arrive = 'set_pot'


class Results1(Page):
    pass

class punishment_part(Page):

    form_model = 'player'
    def get_form_fields(self):
        if self.group.type == 'pun_partisan' or self.group.type == 'pun_control':
            if self.player.label == 'A':
                return ['punishB', 'punishC']
            if self.player.label == 'B':
                return ['punishA', 'punishC']
            if self.player.label == 'C':
                return ['punishA', 'punishB']
        else:
            return []

page_sequence = [MyWaitPage, partisan, GroupWaitPage, group_display, ResultsWaitPage, Results1, punishment_part]
