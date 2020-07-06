from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class Main(Page):
    form_model = 'player'
    form_fields = ['sent_tokens', 'private_tokens']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    def group_total(self):
        return dict(
         group_pot = group_pot + (self.sent_tokens*11 -((1/16)(self.sent_tokens)*(self.sent_tokens)))
         )


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
