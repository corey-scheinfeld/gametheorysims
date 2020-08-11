from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number==1 or self.round_number==6

class setJar(WaitPage):
    after_all_players_arrive = 'create_jar'

class Main(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Introduction,
    setJar,
    Main,
    ResultsWaitPage,
    Results
]
