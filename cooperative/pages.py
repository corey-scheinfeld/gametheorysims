from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    after_all_players_arrive = 'set_winnings'

class Main(Page):
    live_method = 'live_bid'


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
