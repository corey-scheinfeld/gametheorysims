from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):

    def is_displayed(self):
        return self.round_number== 1 or self.round_number== 6

class IntroductionWaitPage(WaitPage):
    wait_for_all_groups = True
    after_all_players_arrive = 'set_up'


class Main(Page):
    form_model = 'player'
    form_fields = ['choice']

    def vars_for_template(self):
        a = self.round_number - 5
        return dict(a = a)


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
