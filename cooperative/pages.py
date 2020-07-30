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

class ResultsWaitPage(WaitPage):

    players = group.get_players()
    for p in players:
        p.my_page_timeout_seconds = 0
        if self.player.id_in_group != player.id_in_group:
            p.give = self.player.keep
            p.keep = self.player.give


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
