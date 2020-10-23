from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def is_displayed(self):
        return self.round_number== 1 or self.round_number== 6

class IntroductionWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'set_up'


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
    def is_displayed(self):
        return self.group.type == 'pun_partisan'

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




page_sequence = [
    Introduction,
    IntroductionWaitPage,
    Main,
    ResultsWaitPage,
    Results
]
