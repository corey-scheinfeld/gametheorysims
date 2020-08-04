from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1

class Main(Page):
    form_model = 'player'
    form_fields = ['contract']


class Contract(Page):
    form_model = 'player'
    def get_form_fields(self):
        if self.player.contract == 'A and B':
            return ['firmA', 'firmB']
        if self.player.contract == 'B and C':
            return ['firmB', 'firmC']
        if self.player.contract == 'A and C':
            return ['firmA', 'firmC']
        if self.player.contract == 'A, B and C':
            return ['firmA', 'firmB', 'firmC']
    def error_message(self, values):
        if self.player.contract == 'A and B':
            if values[firmA]+ values[firmB] != 90:
                return 'The merger profit must total 90'
        if self.player.contract == 'B and C':
            if values[firmB]+ values[firmC] != 40:
                return 'The merger profit must total 40'
        if self.player.contract == 'A and C':
            if values[firmA]+ values[firmC] != 70:
                return 'The merger profit must total 70'
        if self.player.contract == 'A, B and C':
            if values[firmA]+ values[firmB] + values[firmC] != 100:
                return 'The merger profit must total 100'

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

page_sequence = [Introduction, Main, Contract, ResultsWaitPage, Results]
