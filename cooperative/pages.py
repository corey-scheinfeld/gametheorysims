from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    after_all_players_arrive = 'set_game'

class auction_wait(WaitPage):
    def after_all_players_arrive(self):
        pass


class auction(Page):
    live_method = 'live_auction'

    def get_timeout_seconds(self):
        return self.player.my_page_timeout_seconds

    def is_displayed(self):
        if self.player.offer_accepted = True:
            return False
        else:
            return True
    def before_next_page(self):
        players = self.player.get_others_in_group()
        for p in players:
            p.give = self.player.keep
            p.keep = self.player.give
            p.my_page_timeout_seconds = 0
            self.get_timeout_seconds()

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    auction_wait,
    auction,
    ResultsWaitPage,
    Results
]
