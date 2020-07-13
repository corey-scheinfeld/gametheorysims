from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number==1

class Main(Page):
    form_model = 'player'
    form_fields = ['sent_tokens', 'private_tokens']

    def error_message(self, values):
        print('value is', values)
        if((self.sent_tokens + self.private_tokens) != 20):
            return "Total currency distibution must equal 20"


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'



class Results(Page):
    pass


page_sequence = [
    Introduction,
    Main,
    ResultsWaitPage,
    Results
]
