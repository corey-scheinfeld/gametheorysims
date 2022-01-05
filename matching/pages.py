from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number==1


class Decision(Page):
    form_model = 'player'
    form_fields = ['first', 'second', 'third']

    after_all_players_arrive = 'set_payoffs'

    def error_message(self, values):
        if values['first'] == values['second'] or values['second'] == values['third'] or values['first'] == values['third']:
            return 'Each choice must be unique.'

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Decision,
    ResultsWaitPage,
    Results
]
