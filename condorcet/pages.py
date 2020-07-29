from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number==1 or self.round_number==6

class Main(Page):
    form_fields = ['my_hidden_input']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction1,
    Introduction2,
    Main,
    ResultsWaitPage,
    Results
]
