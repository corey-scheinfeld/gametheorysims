from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    after_all_players_arrive = 'set_winnings'

class auction(Page):
    live_method = 'live_auction'


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    auction,
    ResultsWaitPage,
    Results
]
