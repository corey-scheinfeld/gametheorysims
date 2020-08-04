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

    def before_next_page(self):
        players = self.player.get_others_in_group()
        for p in players:
            self.player.keep = p.give
            self.player.give = p.keep

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
