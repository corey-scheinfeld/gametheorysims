from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):

    def is_displayed(self):
        return self.round_number == 1

class AuctionWait(WaitPage):
    after_all_players_arrive = 'set_values'

class Main(Page):
    form_model = 'player'
    formfields = ['bid']


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [Introduction, AuctionWait, Main, ResultsWaitPage, Results]
