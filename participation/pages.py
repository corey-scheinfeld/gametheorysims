from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def round(self):
        if self.round_number == 1:
            instructions_template = 'participation/instructions.html'
        if self.round_number == 6:
            instructions_template = 'participation/part2.html'

    def is_displayed(self):
        return self.round_number== 1 or self.round_number== 6

class IntroductionWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'set_up'

    def is_displayed(self):
        return self.round_number==[1, 6]


class Main(Page):
    form_model = 'player'
    form_fields = ['choice']


class ResultsWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'set_payoffs'




class Results(Page):
    pass


page_sequence = [
    Introduction,
    IntroductionWaitPage,
    Main,
    ResultsWaitPage,
    Results
]
