from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass

class auction_wait(WaitPage):
    def after_all_players_arrive(self):
        pass


class auction(Page):
    live_method = 'live_auction'

    def get_timeout_seconds(self):
        return self.player.my_page_timeout_seconds


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [
    Introduction,
    auction_wait,
    auction,
    ResultsWaitPage,
    Results
]
