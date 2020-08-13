from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number==1 or self.round_number==6

class setJar(WaitPage):
    after_all_players_arrive = 'create_jar'

class Main(Page):
    form_model = 'player'
    form_fields = ['choice']


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        if self.round_number <= 5:
            self.group.count_votes()
            self.group.part1_decision()
            self.group.set_payoffs()
        elif self.round_number >= 6:
            self.group.count_votes()
            self.group.part2_decision()
            self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Introduction,
    setJar,
    Main,
    ResultsWaitPage,
    Results
]
