from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number==1


class Main(Page):
    form_model = 'player'
    form_fields = ['platform']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
